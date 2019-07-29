from django.db import models
from django.urls import reverse

# Create your models here.


class Posts(models.Model):
    title = models.CharField('TITLE', max_length=200, blank=True)
    description = models.CharField('DESCRIPTION', max_length=1000, blank=True)
    content = models.TextField('CONTENT', null=True)
    create_date = models.DateField('Create_date', auto_now_add=True)
    modify_date = models.DateField('Modify_date', auto_now=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ('-create_date', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notice:post_detail')

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()
