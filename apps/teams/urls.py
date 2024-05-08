from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ParticipantViewSet, TeamViewSet, TeamMembershipViewSet, TimeCountViewSet, RoundRobinViewSet

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'participants', ParticipantViewSet)
router.register(r'team-participant', TeamMembershipViewSet)
router.register(r'time-results', TimeCountViewSet)
router.register(r'round-robin-match', RoundRobinViewSet)

urlpatterns = [
    path('', include(router.urls)), ]
