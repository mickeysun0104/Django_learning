from django.shortcuts import render
from django.http import HttpResponse
from music.models import Music
from music.serializer import MusicSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets

# Create your views here.
def music_view(request):
    return HttpResponse('Enjoy music!')

class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = (IsAuthenticated,)

