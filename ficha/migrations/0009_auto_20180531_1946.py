# Generated by Django 2.0.5 on 2018-05-31 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0008_auto_20180531_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='nprevia',
            field=models.BooleanField(),
        ),
    ]