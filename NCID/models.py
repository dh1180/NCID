from django.urls import reverse
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UserManager(BaseUserManager):
    def create_user(self, username, student_id, password=None):
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
            student_id=student_id,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, student_id, password):
        user = self.create_user(
            username=username,
            password=password,
            student_id=student_id,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(
        verbose_name='username',
        max_length=255,
        unique=True,
    )
    student_id = models.CharField(max_length=5)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['student_id']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class NPC(models.Model):
    author = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100)
    contents = models.TextField()
    time = models.DateTimeField(auto_now_add=True, null=True)
    file = models.FileField(blank=True, null=True)

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


class NPC_university(models.Model):
    author = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100)
    contents = models.TextField()
    time = models.DateTimeField(auto_now_add=True, null=True)
    file = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse('university_detail', args=[str(self.pk)])





