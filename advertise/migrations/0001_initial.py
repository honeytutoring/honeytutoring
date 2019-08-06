# Generated by Django 2.2.3 on 2019-08-06 04:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('region', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_title', models.CharField(default='', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=50)),
                ('profile', models.FileField(blank=True, null=True, upload_to='')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('classified_region_name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='region.ClassifiedRegion')),
                ('region', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='region.Region')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertise.Subject')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
