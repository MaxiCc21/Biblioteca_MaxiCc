# Generated by Django 2.2.13 on 2021-08-02 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0005_autor_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='slug',
        ),
    ]