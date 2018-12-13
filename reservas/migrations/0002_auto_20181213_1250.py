# Generated by Django 2.1.4 on 2018-12-13 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='address',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='description',
        ),
        migrations.AlterField(
            model_name='hotel',
            name='name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clientes.Juridica'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apartamentos.Apartamentos'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
