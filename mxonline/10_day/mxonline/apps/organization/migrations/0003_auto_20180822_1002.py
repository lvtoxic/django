# Generated by Django 2.0.3 on 2018-08-22 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_courseorg_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='course_nums',
            field=models.IntegerField(default=0, verbose_name='课程数'),
        ),
        migrations.AddField(
            model_name='courseorg',
            name='students',
            field=models.IntegerField(default=0, verbose_name='学习人数'),
        ),
    ]
