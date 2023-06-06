# Generated by Django 2.2 on 2020-07-13 14:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0019_auto_20200713_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentaire',
            name='Likes',
        ),
        migrations.AddField(
            model_name='commentaire',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to='list.User'),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Dimanche_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 13, 14, 35, 10, 990224, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Dimanche_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 13, 14, 35, 10, 990224, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Jeudi_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 13, 14, 35, 10, 990224, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Jeudi_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 13, 14, 35, 10, 990224, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Lundi_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 13, 14, 35, 10, 990224, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Lundi_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 13, 14, 35, 10, 990224, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Mardi_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 13, 14, 35, 10, 990224, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Mardi_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 13, 14, 35, 10, 990224, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Mercredi_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 13, 14, 35, 10, 990224, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Mercredi_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 13, 14, 35, 10, 990224, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Samedi_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 13, 14, 35, 10, 990224, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Samedi_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 13, 14, 35, 10, 990224, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Vendredi_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 13, 14, 35, 10, 990224, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Vendredi_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 13, 14, 35, 10, 990224, tzinfo=utc), null=True),
        ),
    ]
