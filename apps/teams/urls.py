from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ParticipantViewSet, TeamViewSet, TeamMembershipViewSet

router = DefaultRouter()
router.register(r'teams', ParticipantViewSet)
router.register(r'participants', TeamViewSet)
router.register(r'teamparticipant', TeamMembershipViewSet)

urlpatterns = [
    path('', include(router.urls)), ]
