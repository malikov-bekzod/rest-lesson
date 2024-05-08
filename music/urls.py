from django.urls import path, include
from .views import LandingPageAPIView,AlbomAPIViewSet,ArtistAPIViewSet,SongAPIViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix="songs", viewset=SongAPIViewSet, basename="songs")
router.register(prefix="alboms", viewset=AlbomAPIViewSet, basename="alboms")
router.register(prefix="artists", viewset=ArtistAPIViewSet, basename="artist")

urlpatterns = [
    path("landing/", LandingPageAPIView.as_view(), name="landing"),
    path("", include(router.urls)),
]
