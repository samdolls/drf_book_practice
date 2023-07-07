from django.urls import path
from .views import *

app_name = "practice"
urlpatterns = [
    path('books', BooksAPI.as_view()),
    path('book/<int:book_id>', BookAPI.as_view()),
]