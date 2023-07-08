from django.urls import path
from .views import *

app_name = "chapter5"
urlpatterns = [
    path('', TodosAPIView.as_view()),
    path('<int:todo_id>', TodoAPIView.as_view()),
    path('done', DoneTodosAPIView.as_view()),
    path('<int:todo_id>/done', DoneTodoAPIView.as_view()),
]