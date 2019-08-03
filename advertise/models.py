from django.conf import settings
from django.db import models
from accounts.models import Users
from django.shortcuts import reverse


class Region(models.Model):
    area = models.CharField(max_length=4, blank=False, default='')

    def __str__(self):
        return self.area


class Subject(models.Model):
    subject_title = models.CharField(max_length=4, blank=False, default='')

    def __str__(self):
        return self.subject_title


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    objects = models.Manager()
    title = models.CharField(max_length=30)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    profile = models.FileField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    modify_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('advertise:detail', kwargs={'pk': self.pk})

