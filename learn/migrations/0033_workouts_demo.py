# Generated by Django 5.0.1 on 2024-03-26 17:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("learn", "0032_remove_workouts_demo_alter_correctexerciseform_demo_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="workouts",
            name="demo",
            field=models.ImageField(default=django.utils.timezone.now, upload_to=""),
            preserve_default=False,
        ),
    ]
