from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=11, blank=True)
    GENDER_MAIL, GENDER_FEMAIL = 0, 1
    GENDER_OPTION = (
        (GENDER_MAIL, '남성'),
        (GENDER_FEMAIL, '여성')
    )
    sex = models.SmallIntegerField(choices=GENDER_OPTION, null=True)
    USER_TEACHER, USER_STUDENT, USER_PARENT = 0, 1, 2
    USER_TYPE = (
        (USER_TEACHER, '선생님'),
        (USER_STUDENT, '학생'),
        (USER_PARENT, '학부모'),
    )
    user_type = models.SmallIntegerField(choices=USER_TYPE, null=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    def is_teacher(self):
        return hasattr(self, 'teacher') and self.user_type == Users.USER_TEACHER


class Teacher(models.Model):
    user = models.OneToOneField('accounts.Users', on_delete=models.CASCADE, related_name='teacher')
    university = models.CharField(max_length=20)
    subjects = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.user.first_name


class Student(models.Model):
    user = models.OneToOneField('accounts.Users', on_delete=models.CASCADE, related_name='student')
    school = models.CharField(max_length=15)
    year = models.CharField(max_length=5)

    def __str__(self):
        return self.user.first_name

