# Generated by Django 4.0.4 on 2022-04-29 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m7_python', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmuebles',
            name='m2_terreno',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='inmuebles',
            name='numero_est',
            field=models.IntegerField(default=0),
        ),
    ]
