from django.db import models

# Create your models here.
class Todo(models.Model):
    todo_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 50)
    description = models.TextField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    complete = models.BooleanField(default = False)
    important = models.BooleanField(default = False)

    def __str__(self):
        return self.title
