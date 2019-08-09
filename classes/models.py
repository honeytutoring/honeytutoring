from django.db import models


class Class(models.Model):
    class_teacher = models.ForeignKey('accounts.Teacher', on_delete=models.CASCADE, related_name='classes', null=True)
    students = models.ManyToManyField('accounts.Student', related_name='classes')
    class_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    subject = models.CharField(max_length=5)
    etc = models.CharField(max_length=200, blank=True, default='')
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.class_name


class Schedule(models.Model):
    klass = models.ForeignKey('classes.Class', on_delete=models.CASCADE, related_name='schedules')
    start_date = models.DateField()
    end_date = models.DateField()
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Memo(models.Model):
    klass = models.ForeignKey('classes.Class', on_delete=models.CASCADE, related_name='memo')
    content = models.CharField(max_length=250)

    def __str__(self):
        return self.content
