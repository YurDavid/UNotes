from django.shortcuts import render

# Create your views here.
from .models import Note
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from rest_framework import status


@api_view(["GET", "POST"])
def notes_list(request):
    if request.method == "POST":
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data={"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    else:
        notes = Note.objects.all()
        serializer = NoteSerializer(notes,many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(["PUT"])
def notes_detail(request, pk):
    try:
        notes = Note.objects.get(pk=pk)
    except Lyric.DoesNotExist:
        return Response(data={"error": "Notes not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = NoteSerializer(notes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data={"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

