# Generated by Django 3.2.18 on 2023-05-17 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tundorul', '0009_alter_suggestions_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suggestions',
            name='slug',
        ),
        migrations.AlterField(
            model_name='suggestions',
            name='title',
            field=models.TextField(unique=True),
        ),
    ]