# Generated by Django 4.2.8 on 2023-12-26 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("relecloud", "0005_opinion"),
    ]

    operations = [
        migrations.AddField(
            model_name="destination",
            name="image",
            field=models.ImageField(default=0, upload_to="destination_images/"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="destination",
            name="slug",
            field=models.SlugField(default=0),
            preserve_default=False,
        ),
    ]
