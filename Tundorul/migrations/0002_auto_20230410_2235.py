# Generated by Django 3.2.18 on 2023-04-10 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tundorul', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['-username']},
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='join_date',
            new_name='following_since',
        ),
    ]
