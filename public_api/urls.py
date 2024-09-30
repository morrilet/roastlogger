from rest_framework.routers import DefaultRouter
from public_api.views import CoffeeViewSet, RecipeViewSet, RoastViewSet, EventViewSet, NoteViewSet

router = DefaultRouter()
router.register("coffee", CoffeeViewSet)
router.register("recipe", RecipeViewSet)
router.register("roast", RoastViewSet)
router.register("event", EventViewSet)
router.register("note", NoteViewSet)
urlpatterns = router.urls