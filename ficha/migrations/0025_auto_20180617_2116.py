# Generated by Django 2.0.5 on 2018-06-18 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0024_auto_20180617_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='altura',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
