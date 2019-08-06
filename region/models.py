from django.db import models


class Region(models.Model):
    area = models.CharField(max_length=4, blank=False, default='', null=True)

    def __str__(self):
        return self.area


class ClassifiedRegion(models.Model):
    region = models.ForeignKey('region.Region', on_delete=models.CASCADE, related_name='classified_regions')
    classified_region = models.CharField(max_length=5, blank=False, default='')

    def __str__(self):
        return self.classified_region

