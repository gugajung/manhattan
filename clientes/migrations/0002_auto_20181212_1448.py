# Generated by Django 2.1.4 on 2018-12-12 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juridica',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='juridica',
            name='estado_civil',
        ),
        migrations.RemoveField(
            model_name='juridica',
            name='rg',
        ),
    ]
