# Generated by Django 3.2.18 on 2023-05-01 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='senha',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='nome',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='cidade',
        ),
        migrations.RemoveField(
            model_name='user',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='user',
            name='numero',
        ),
        migrations.RemoveField(
            model_name='user',
            name='sobrenome',
        ),
        migrations.RemoveField(
            model_name='user',
            name='telefone',
        ),
    ]
