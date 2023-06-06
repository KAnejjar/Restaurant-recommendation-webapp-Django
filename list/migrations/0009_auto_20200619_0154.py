# Generated by Django 2.1.5 on 2020-06-18 23:54

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0008_auto_20200619_0148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heurestravail',
            name='Nom',
        ),
        migrations.AddField(
            model_name='restau',
            name='HeuresTrv',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='list.HeuresTravail'),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Dimanche_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 18, 23, 54, 9, 833938, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Dimanche_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 18, 23, 54, 9, 833938, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Jeudi_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 18, 23, 54, 9, 833938, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Jeudi_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 18, 23, 54, 9, 833938, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Lundi_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 18, 23, 54, 9, 833938, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Lundi_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 18, 23, 54, 9, 833938, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Mardi_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 18, 23, 54, 9, 833938, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Mardi_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 18, 23, 54, 9, 833938, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Mercredi_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 18, 23, 54, 9, 833938, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Mercredi_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 18, 23, 54, 9, 833938, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Samedi_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 18, 23, 54, 9, 833938, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Samedi_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 18, 23, 54, 9, 833938, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Vendredi_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 18, 23, 54, 9, 833938, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Vendredi_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 18, 23, 54, 9, 833938, tzinfo=utc), null=True),
        ),
    ]
