# Generated by Django 5.1.1 on 2024-10-06 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=120)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
    ]