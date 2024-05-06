from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ParticipantViewSet, TeamViewSet, TeamMembershipViewSet, TimeCountViewSet

router = DefaultRouter()
router.register(r'teams', ParticipantViewSet)
router.register(r'participants', TeamViewSet)
router.register(r'team-participant', TeamMembershipViewSet)
router.register(r'time-results', TimeCountViewSet)

urlpatterns = [
    path('', include(router.urls)), ]
