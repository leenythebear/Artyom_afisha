# Generated by Django 3.2 on 2023-02-12 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_alter_image_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='slug',
        ),
    ]
