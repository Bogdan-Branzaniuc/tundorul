# Generated by Django 3.2.18 on 2023-05-17 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tundorul', '0011_suggestions_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suggestions',
            name='author_profile_img',
        ),
        migrations.AlterField(
            model_name='suggestions',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]
