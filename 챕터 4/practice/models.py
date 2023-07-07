from django.db import models

# Create your models here.
class Book(models.Model):
    bid = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)