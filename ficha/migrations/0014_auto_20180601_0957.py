# Generated by Django 2.0.5 on 2018-06-01 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0013_auto_20180601_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficha',
            name='cardio_arr',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='cardio_cor',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='cardio_has',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='cardio_icc',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='cardio_neg',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='cardio_out',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='endocrino_dia',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='endocrino_dlp',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='endocrino_dti',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='endocrino_neg',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='endocrino_out',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='gastro_gas',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='gastro_neg',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='gastro_obs',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='gastro_out',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='gastro_rge',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='gastro_vom',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='hem_ane',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='hem_coa',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='hem_hep',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='hem_hiv',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='hem_neg',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='hem_out',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='hem_tra',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='musc_ati',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='musc_ato',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='musc_des',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='musc_dis',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='musc_lom',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='musc_neg',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='musc_out',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='neuro_avc',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='neuro_cef',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='neuro_con',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='neuro_lme',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='neuro_neg',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='neuro_out',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='renal_dia',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='renal_ira',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='renal_irc',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='renal_neg',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='renal_out',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='resp_asm',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='resp_dpo',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='resp_iva',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='resp_neg',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='resp_out',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='ficha',
            name='resp_tbg',
            field=models.NullBooleanField(),
        ),
    ]