from django.shortcuts import render

from rest_framework import viewsets, generics
from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()


class NotesGet(generics.ListAPIView):  # get all
    serializer_class = NoteSerializer
    queryset = Note.objects.all()


class NoteGet(generics.RetrieveAPIView):  # get specific
    serializer_class = NoteSerializer
    queryset = Note.objects.all()


class NotePost(generics.CreateAPIView):  # post
    serializer_class = NoteSerializer
    queryset = Note.objects.all()


class NotePut(generics.UpdateAPIView):  # put
    serializer_class = NoteSerializer
    queryset = Note.objects.all()


class NoteDelete(generics.DestroyAPIView):  # delete
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
