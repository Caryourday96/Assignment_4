# Generated by Django 2.0.3 on 2018-03-23 20:34
#ADETUNJI KAYODE

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0003_auto_20180323_1804'),
    ]

    operations = [
        migrations.RenameField(
            model_name='industry',
            old_name='commod',
            new_name='COMMOD',
        ),
        migrations.RenameField(
            model_name='industry',
            old_name='coordinate',
            new_name='Coordinate',
        ),
        migrations.RenameField(
            model_name='industry',
            old_name='geo',
            new_name='GEO',
        ),
        migrations.RenameField(
            model_name='industry',
            old_name='ref_date',
            new_name='Ref_Date',
        ),
        migrations.RenameField(
            model_name='industry',
            old_name='value',
            new_name='Value',
        ),
        migrations.RenameField(
            model_name='industry',
            old_name='vector',
            new_name='Vector',
        ),
    ]