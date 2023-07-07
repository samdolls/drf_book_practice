from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer

from django.shortcuts import get_object_or_404

# Create your views here.
class BooksAPI(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
        return Response(serializer.data)
    
class BookAPI(APIView):
    def get(self, request, book_id):
        book = get_object_or_404(Book, pk = book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data)