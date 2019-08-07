from django.db import models
from django.urls import reverse

# Create your models here.

class QandA(models.Model):
    objects = models.Manager()
    title = models.CharField('TITLE',max_length=200, blank=True)
    content = models.TextField('CONTENT',null=True)
    answer = models.CharField('ANSWER', max_length=200, null=True, blank=True)
    create_date = models.DateField('Create_date', auto_now_add=True)
    modify_date = models.DateField('Modify_date', auto_now=True)
    answer_registered = models.CharField(default='답변대기',max_length=10)

    # def get_absolute_url(self):
    #     return reverse('notice:q_a_detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.title
