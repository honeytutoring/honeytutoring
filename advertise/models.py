from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.
class Post(models.Model):
    # user = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    objects = models.Manager()
    title = models.CharField(max_length=30)
    region = models.CharField(max_length=10)
    subject = models.CharField(max_length=10)
    content = models.CharField(max_length=50)
    profile = models.FileField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add = True, auto_now = False)

    class Meta:
       ordering = ['-created'] 
    
    def __str__(self):
        return self.title
        

    def get_absolute_url(self):
        return reverse('advertise:detail',args=[str(self.pk)])
