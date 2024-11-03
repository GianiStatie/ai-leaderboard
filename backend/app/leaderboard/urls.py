from django.urls import path, include
from rest_framework import routers

from .views import TeamViewSet, ScoreViewSet, ScoreHistoryViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'score', ScoreViewSet)
router.register(r'score_history', ScoreHistoryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]