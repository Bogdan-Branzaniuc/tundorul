# Generated by Django 3.2.18 on 2023-03-22 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0003_extra_data_default_dict'),
        ('Tundorul', '0002_auto_20230322_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile_related', to='socialaccount.socialaccount'),
        ),
    ]