# Generated by Django 5.0.6 on 2024-06-24 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_userprofile_nome_empresa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='github',
            new_name='whatsapp',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='twitch',
        ),
    ]
