# Generated by Django 5.0.6 on 2024-06-23 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_userprofile_custom_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='custom_url',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
