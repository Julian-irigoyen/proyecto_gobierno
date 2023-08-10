# Generated by Django 4.2.3 on 2023-07-21 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitudes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=300, verbose_name='Titulo')),
                ('solicitante', models.CharField(max_length=300, verbose_name='Solicitante')),
                ('fecha_solicitud', models.DateField(verbose_name='Fecha de solicitud')),
            ],
        ),
    ]
