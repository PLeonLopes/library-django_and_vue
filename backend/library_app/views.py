from django.shortcuts import render
from rest_framework import generics         # import para uso das generics views
from .models import Book
from .serializers import BookSerializer

# Create your views here.

# Create
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Read, Update, Delete
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    