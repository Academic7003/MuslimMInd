from django.db import models


class Creator(models.Model):
    name = models.CharField(max_length=20)


    def __str__(self):
        return str(self.name)