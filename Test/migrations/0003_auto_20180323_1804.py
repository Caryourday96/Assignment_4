# Generated by Django 2.0.3 on 2018-03-23 18:04
#ADETUNJI KAYODE

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0002_auto_20180323_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='industry',
            name='coordinate',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='industry',
            name='ref_date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='industry',
            name='value',
            field=models.CharField(max_length=100),
        ),
    ]
