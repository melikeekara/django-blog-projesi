# Generated by Django 4.2.2 on 2023-06-29 14:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bloge', '0011_remove_kategorimodel_soyadı_kategorimodel_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kategorimodel',
            name='slug',
        ),
        migrations.AddField(
            model_name='kategorimodel',
            name='soyadı',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
        ),
    ]
