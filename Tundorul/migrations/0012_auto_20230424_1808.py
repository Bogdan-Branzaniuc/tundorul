# Generated by Django 3.2.18 on 2023-04-24 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tundorul', '0011_remove_streamschedule_twitch_segment_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='streamschedule',
            options={'ordering': ['start_time']},
        ),
        migrations.RemoveField(
            model_name='streamschedule',
            name='day',
        ),
    ]