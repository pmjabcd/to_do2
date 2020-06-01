from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post (models. Model):
    title = models. CharField(max_length=30)
    content = models. TextField()
    due_date = models. DateTimeField
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

def __str__ (self):
    return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='a_comments')
