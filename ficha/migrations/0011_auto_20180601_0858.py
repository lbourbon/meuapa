# Generated by Django 2.0.5 on 2018-06-01 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0010_auto_20180601_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='altura',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='imc',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='peso',
            field=models.FloatField(blank=True, null=True),
        ),
    ]