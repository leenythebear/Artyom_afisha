# Generated by Django 4.1.7 on 2023-02-15 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0013_alter_image_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="image",
            field=models.ImageField(upload_to="img/"),
        ),
    ]