# Generated by Django 5.0.1 on 2024-02-02 12:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("learn", "0006_alter_coursecomments_comment_by"),
    ]

    operations = [
        migrations.AddField(
            model_name="workouts",
            name="demo",
            field=models.URLField(blank=True, null=True),
        ),
    ]
