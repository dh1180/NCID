from django.db import models
from django.urls import reverse

# Create your models here.


class NPC(models.Model):
    author = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100)
    contents = models.TextField()
    time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse('detail', args=[str(self.pk)])


class NPC_bookmark(models.Model):
    author = models.CharField(max_length=100, null=True)
    url_title = models.CharField(max_length=100)
    url = models.URLField(max_length=500)
    time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.url_title

    def get_absolute_url(self):

        return reverse('bookmark_detail', args=[str(self.pk)])

class NPC_school(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse('school_detail', args=[str(self.pk)])






