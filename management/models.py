from django.db import models
from honey import settings


class Class(models.Model):
    class_teacher = models.ForeignKey('accounts.Teacher', on_delete=models.CASCADE, related_name='classes', null=True)
    students = models.ManyToManyField('accounts.Student', related_name='classes')
    class_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    subject = models.CharField(max_length=5)
    memo = models.TextField()
    etc = models.CharField(max_length=200, blank=True, default='')
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.class_name

