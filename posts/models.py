from django.db import models
from creators.models import Creator



class PostModel(models.Model):
    title = models.CharField(max_length=255)
    created_data = models.DateTimeField(auto_now_add=True)
    creators = models.ManyToManyField(Creator)
    body = models.TextField()
    file = models.FileField()

