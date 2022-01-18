import random

from django.http import HttpResponseRedirect
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from art.serializer import ArtSerializer
from art.models import Art


class GetAllArtsAPI(ListAPIView):
    serializer_class = ArtSerializer
    queryset = Art.objects.all().order_by('?')
    filterset_fields = ['artist', 'title', 'year', 'type', 'location']
    ordering_fields = ['id', 'artist', 'title', 'year', 'type', 'location', '?']


class GetArtAPI(RetrieveAPIView):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer


class GetARandomArtAPI(APIView):

    def get(self, requests, *args, **kwargs):
        queryset = random.choice(Art.objects.all())
        return Response(ArtSerializer(queryset).data)


class GetARandomArtPictureAPI(APIView):

    def get(self, requests, *args, **kwargs):
        queryset = random.choice(Art.objects.all())
        return HttpResponseRedirect(ArtSerializer(queryset).data['picture'])
