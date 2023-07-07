from django.urls import path
from rest_framework import routers
from .views import *

app_name = "practice"

router = routers.SimpleRouter()
router.register('books', BookViewSet)

# urlpatterns = [
#     # path('', BooksAPIGenerics.as_view()),
#     # path('<int:book_id>', BookAPIGenerics.as_view()),
# ]

urlpatterns = router.urls