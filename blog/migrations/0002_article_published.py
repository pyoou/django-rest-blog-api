# Generated by Django 3.2.2 on 2021-05-08 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='published',
            field=models.CharField(choices=[('public', 'public'), ('private', 'private')], default='private', max_length=7),
        ),
    ]
