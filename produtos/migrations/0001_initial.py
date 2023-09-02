# Generated by Django 3.2.18 on 2023-09-01 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nome_produto', models.CharField(max_length=30)),
                ('descricao', models.TextField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='img_produtos')),
            ],
        ),
    ]