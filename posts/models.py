
from uuid import uuid4
from django.db import models
from creators.models import Creator

def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'mind_archive/{filename}'.format(
        filename='{}.{}'.format(uuid4().hex, ext)
    )
    return file_path



class PostModel(models.Model):
    title = models.CharField(max_length=255)
    created_data = models.DateTimeField(auto_now_add=True)
    creators = models.ForeignKey(Creator, on_delete=models.SET_NULL, null=True, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    file = models.FileField(upload_to=upload_location, null=True, blank=True)
    sees = models.PositiveSmallIntegerField(default=0)
    downloads = models.PositiveSmallIntegerField(default=0)
    is_top = models.BooleanField(null=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url

    @property
    def fileURL(self):
        try:
            url = str(self.file.url)
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.title)
