# Generated by Django 5.0.1 on 2024-06-12 12:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("learn", "0056_image"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Image",
        ),
        migrations.RemoveField(
            model_name="blog",
            name="status",
        ),
        migrations.AlterField(
            model_name="blog",
            name="title",
            field=models.CharField(max_length=300),
        ),
    ]
