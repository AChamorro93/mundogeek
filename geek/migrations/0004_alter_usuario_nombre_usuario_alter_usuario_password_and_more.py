# Generated by Django 5.1.1 on 2024-10-11 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geek', '0003_producto_alter_usuario_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nombre_usuario',
            field=models.CharField(max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
