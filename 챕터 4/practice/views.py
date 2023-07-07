from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions, generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer

from django.shortcuts import get_object_or_404

# Create your views here.
# FBV
# @api_view(['GET', 'POST'])
# def book_list_create(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many = True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = BookSerializer(data = request.data)
#         if serializer.is_valid(raise_exception = True):
#             serializer.save()
#         return Response(serializer.data)
    
# @api_view(['GET', 'PATCH', 'DELETE'])
# def book_detail_update_delete(request, book_id):
#     book = get_object_or_404(Book, pk = book_id)

#     if request.method == 'GET':
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
    
#     elif request.method == 'PATCH':
#         serializer = BookSerializer(instance = book, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
    
#     elif request.method == 'DELETE':
#         book.delete()
#         data = {
#             'deleted_book' : book_id,
#         }
#         return Response(data)

# CBV
# class BooksAPI(APIView):
#     def get(self, request):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many = True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = BookSerializer(data = request.data)
#         if serializer.is_valid(raise_exception = True):
#             serializer.save()
#         return Response(serializer.data)
    
# class BookAPI(APIView):
#     def get(self, request, book_id):
#         book = get_object_or_404(Book, pk = book_id)
#         serializer = BookSerializer(book)
#         return Response(serializer.data)

# Mixins
# class BooksAPIMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class BookAPIMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = 'book_id'

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def patch(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# Generics
class BooksAPIGenerics(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookAPIGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'book_id'

# ViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
