# Generated by Django 3.2.18 on 2023-05-18 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tundorul', '0014_auto_20230518_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='join_date',
            field=models.DateField(blank=True),
        ),
    ]