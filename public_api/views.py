from rest_framework.viewsets import ModelViewSet
from recipes.models import Coffee, Recipe, Roast, Event, Note
from public_api.serializers import CoffeeSerializer, RecipeSerializer, RoastSerializer, EventSerializer, NoteSerializer


class CoffeeViewSet(ModelViewSet):
    model = Coffee
    serializer_class = CoffeeSerializer
    queryset = Coffee.objects.all()


class RecipeViewSet(ModelViewSet):
    model = Recipe
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


class RoastViewSet(ModelViewSet):
    model = Roast
    serializer_class = RoastSerializer
    queryset = Roast.objects.all()


class EventViewSet(ModelViewSet):
    model = Event
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class NoteViewSet(ModelViewSet):
    model = Note
    serializer_class = NoteSerializer
    queryset = Note.objects.all()