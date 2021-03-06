# Generated by Django 2.1.4 on 2018-12-13 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apartamentos', '0002_auto_20181213_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='apartamentos',
            name='numero_apto',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='apartamentos',
            name='pertence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='apartamentos.Hotel'),
        ),
        migrations.AlterField(
            model_name='apartamentos',
            name='ramal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='apartamentos',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='apartamentos.Tag'),
        ),
    ]
