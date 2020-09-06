from django.db import models
from django.urls import reverse

# Create your models here.


class NPC(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse('detail', args=[str(self.pk)])


class NPC_bookmark(models.Model):
    url_title = models.CharField(max_length=100)
    url = models.URLField(max_length=500)

    def get_absolute_url(self):

        return reverse('bookmark_detail', args=[str(self.pk)])








