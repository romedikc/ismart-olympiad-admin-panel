from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SubcategoryViewSet, RaceViewSet, ParticipantViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubcategoryViewSet)
router.register(r'races', RaceViewSet)
router.register(r'participants', ParticipantViewSet)

urlpatterns = [
    path('', include(router.urls)),
]