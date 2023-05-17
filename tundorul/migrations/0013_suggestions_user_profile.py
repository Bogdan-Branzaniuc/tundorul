# Generated by Django 3.2.18 on 2023-05-17 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tundorul', '0012_auto_20230517_0331'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestions',
            name='user_profile',
            field=models.ForeignKey(default=15, on_delete=django.db.models.deletion.CASCADE, related_name='suggestion', to='tundorul.userprofile'),
            preserve_default=False,
        ),
    ]