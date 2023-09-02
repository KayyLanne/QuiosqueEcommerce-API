# Generated by Django 3.2.18 on 2023-04-30 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('sobrenome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('senha', models.CharField(max_length=10)),
                ('telefone', models.CharField(max_length=10)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('numero', models.IntegerField(null=True)),
            ],
        ),
    ]
