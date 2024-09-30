from datetime import datetime, timedelta
from django.test import TestCase
from recipes.models import Coffee, Recipe, Roast, Event, Note
from django.core.exceptions import ValidationError


class CoffeeTestCase(TestCase):
    def setUp(self):
        pass


class RecipeTestCase(TestCase):
    def setUp(self):
        self.coffee = Coffee.objects.create(name="Test Coffee")

    def test_target_percent_range_start_gte_0(self):
        with self.assertRaises(ValidationError):
            Recipe.objects.create(
                name = "Test Recipe",
                coffee = self.coffee,
                target_percent_range_start = -1,
                target_percent_range_end = 10,
            )

    def test_target_percent_range_start_0(self):
        Recipe.objects.create(
            name = "Test Recipe",
            coffee = self.coffee,
            target_percent_range_start = 0,
            target_percent_range_end = 10,
        )

    def test_target_percent_range_start_100(self):
        Recipe.objects.create(
            name = "Test Recipe",
            coffee = self.coffee,
            target_percent_range_start = 100,
            target_percent_range_end = 10,
        )
    
    def test_target_percent_range_start_lte_100(self):
        with self.assertRaises(ValidationError):
            Recipe.objects.create(
                name = "Test Recipe",
                coffee = self.coffee,
                target_percent_range_start = 101,
                target_percent_range_end = 10,
            )

    def test_target_percent_range_end_gte_0(self):
        with self.assertRaises(ValidationError):
            Recipe.objects.create(
                name = "Test Recipe",
                coffee = self.coffee,
                target_percent_range_end = -1,
                target_percent_range_start = 10,
            )

    def test_target_percent_range_end_0(self):
        Recipe.objects.create(
            name = "Test Recipe",
            coffee = self.coffee,
            target_percent_range_end = 0,
            target_percent_range_start = 10,
        )

    def test_target_percent_range_end_100(self):
        Recipe.objects.create(
            name = "Test Recipe",
            coffee = self.coffee,
            target_percent_range_end = 100,
            target_percent_range_start = 10,
        )

    def test_target_percent_range_end_lte_100(self):
        with self.assertRaises(ValidationError):
            Recipe.objects.create(
                name = "Test Recipe",
                coffee = self.coffee,
                target_percent_range_end = 101,
                target_percent_range_start = 10,
            )


class RoastTestCase(TestCase):
    def setUp(self):
        self.coffee = Coffee.objects.create(name="Test Coffee")
        self.recipe = Recipe.objects.create(
            name = "Test Recipe", 
            coffee = self.coffee, 
            target_percent_range_start = 0, 
            target_percent_range_end = 1
        )

    def test_roast_manual_date_on_create(self):
        date = datetime.now() - timedelta(days=1)
        roast = Roast.objects.create(
            date = date,
            recipe = self.recipe,
            input_grams = 1,
            output_grams = 1,
        )
        self.assertEqual(date, roast.date)

    def test_roast_input_lt_0(self):
        with self.assertRaises(ValidationError):
            Roast.objects.create(
                recipe = self.recipe,
                input_grams = -1,
                output_grams = 1,
            )

    def test_roast_input_0(self):
        Roast.objects.create(
            recipe = self.recipe,
            input_grams = 0,
            output_grams = 1,
        )

    def test_roast_output_lt_0(self):
        with self.assertRaises(ValidationError):
            Roast.objects.create(
                recipe=self.recipe,
                input_grams=1,
                output_grams=-1,
            )

    def test_roast_output_0(self):
        Roast.objects.create(
            recipe=self.recipe,
            input_grams=1,
            output_grams=0,
        )


class EventTestCase(TestCase):
    def setUp(self):
        pass


class NoteTestCase(TestCase):
    def setUp(self):
        pass