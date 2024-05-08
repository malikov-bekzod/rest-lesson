from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from .models import Artist,Albom,Song
from .serializers import ArtistSerializer,AlbomSerializer,SongSerializer
# Create your views here.

class LandingPageAPIView(APIView):
    def get(self,request):
        return Response(data = {"msg":"you are in langding page"})
    
    def post(self,request):
        return Response(data={"xabar":"this is post method"})


class ArtistAPIViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ["name"]
    pagination_class = LimitOffsetPagination


class AlbomAPIViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ["title"]
    pagination_class = LimitOffsetPagination


class SongAPIViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ["title"]
    pagination_class = LimitOffsetPagination
