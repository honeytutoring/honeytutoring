from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.shortcuts import reverse


class University(models.Model):
    university_title = models.CharField(max_length=20, blank=False, default='')
    university_email = models.EmailField(blank=True)

    def __str__(self):
        return self.university_title


class Users(AbstractUser):

    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=11, blank=True)
    GENDER_MAIL = 'M'
    GENDER_FEMAIL = 'W'
    GENDER_OPTION = ((GENDER_MAIL, '남성'), (GENDER_FEMAIL, '여성'))
    sex = models.CharField(max_length=1, choices=GENDER_OPTION, blank=True, default='')
    TYPE_TEACHER = 'T'
    TYPE_STUDENT = 'S'
    TYPE_PARENT = 'P'
    USER_TYPE_OPTION = (
        (TYPE_TEACHER, '선생님'),
        (TYPE_STUDENT, '학생'),
        (TYPE_PARENT, '학부모'),
    )
    user_type = models.CharField(max_length=1, choices=USER_TYPE_OPTION, blank=True, default='')
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
