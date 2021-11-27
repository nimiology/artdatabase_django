import random

from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from art.api.serializer import ArtSerializer
from art.models import Art


class GetAllArtsAPI(ListAPIView):
    serializer_class = ArtSerializer
    queryset = Art.objects.all()
    filterset_fields = ['painter', 'title', 'year', 'type', 'location']
    ordering_fields = ['painter', 'title', 'year', 'type', 'location']


class GetArtAPI(RetrieveAPIView):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer


class GetARandomArtAPI(APIView):
    def get(self, requests, *args, **kwargs):
        queryset = random.choice(Art.objects.all())
        return Response(ArtSerializer(queryset).data)