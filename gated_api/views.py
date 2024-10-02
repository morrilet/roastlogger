from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from recipes.models import Coffee, Recipe, Roast, Event, Note
from gated_api.serializers import CoffeeSerializer, RecipeSerializer, RoastSerializer, EventSerializer, NoteSerializer


# TODO: This is fine for now, but ideally we can just blanket-apply this logic to all URLs from this app.
#       Look into doing that once things are more or less working and users can create accounts.
# class GatedModelViewSet(ModelViewSet):    
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]


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