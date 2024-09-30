from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

# Quick breakdown here - update if relationships change significantly!
# https://excalidraw.com/#json=-6ROD6mlSwcM62ENFsTEV,C7EVihnDZ0HPabuqg4C8-Q

class Recipe(models.Model):
    name = models.CharField(max_length=256)
    coffee = models.ForeignKey(to="recipes.coffee", on_delete=models.CASCADE)

    # Moisture % range
    target_percent_range_start = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])
    target_percent_range_end = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])

    def save(self, *args, **kwargs):
        # Validate fields on manual saves.
        self.full_clean()
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Coffee(models.Model):
    name = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name


class Roast(models.Model):
    date = models.DateTimeField(default=timezone.now)
    recipe = models.ForeignKey(to="recipes.recipe", on_delete=models.CASCADE)
    input_grams = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(0)])
    output_grams = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(0)])

    @property
    def moisture_loss_percent(self):
        pass

    def save(self, *args, **kwargs):
        # Validate fields on manual saves.
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.recipe.name} - {self.date}"

class Event(models.Model):

    EVENT_TYPE_LOG = "LG"
    EVENT_TYPE_DRY_END = "DE"
    EVENT_TYPE_FIRST_CRACK = "FC"
    EVENT_TYPE_SECOND_CRACK = "SC"
    EVENT_TYPE_DROP = "DR"
    EVENT_TYPES = (
        (EVENT_TYPE_LOG, "Log"),
        (EVENT_TYPE_DRY_END, "Dry End"),
        (EVENT_TYPE_FIRST_CRACK, "First Crack"),
        (EVENT_TYPE_SECOND_CRACK, "Second Crack"),
        (EVENT_TYPE_DROP, "Drop"),
    )

    event_type = models.CharField(max_length=2, choices=EVENT_TYPES, default=EVENT_TYPE_LOG)
    degrees_celcius = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    roast = models.ForeignKey(to="recipes.roast", on_delete=models.CASCADE)


class Note(models.Model):
    class Meta:
        # Generic FKs don't generate indices as normal, so index on type / ID manually.
        indexes = [
            models.Index(fields=["content_type", "object_id"])
        ]

    ### -~-~-~-~- Start GenericForeignKey Setup

    # Limit the types of models we can stick notes on. This should be easy to expand as needed.
    notable_models = (
        models.Q(app_label="recipes", model="recipe") | 
        models.Q(app_label="recipes", model="coffee") | 
        models.Q(app_label="recipes", mdoel="event")
    )

    # Generic key fields for the note-able objects we care about.
    content_type = models.ForeignKey(to=ContentType, on_delete=models.CASCADE, limit_choices_to=notable_models)
    object_id = models.PositiveIntegerField()

    # Use the columns we created above to construct the generic key.
    content_object = GenericForeignKey("content_type", "object_id") 

    ### -~-~-~-~- End GenericForeignKey Setup

    description = models.TextField()
