from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Picture(models.Model):
    image = models.ImageField(upload_to = 'pics/static/images')
    file_name = models.CharField(max_length=200)
    def __str__(self):
        return self.file_name