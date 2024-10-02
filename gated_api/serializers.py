from rest_framework.serializers import ModelSerializer
from recipes.models import Coffee, Recipe, Roast, Event, Note

class CoffeeSerializer(ModelSerializer):
    class Meta:
        model = Coffee
        fields = "__all__"


class RecipeSerializer(ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"


class RoastSerializer(ModelSerializer):
    class Meta:
        model = Roast
        fields = "__all__"


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"
        