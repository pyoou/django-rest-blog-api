# Generated by Django 3.2.2 on 2021-05-08 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='background_image',
        ),
    ]