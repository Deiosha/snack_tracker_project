# Generated by Django 4.2.2 on 2023-06-15 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("things", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="thing",
            name="description",
            field=models.TextField(default=""),
        ),
    ]
