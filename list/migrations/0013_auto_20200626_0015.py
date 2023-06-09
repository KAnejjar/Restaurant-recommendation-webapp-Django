# Generated by Django 2.2 on 2020-06-25 22:15

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0012_auto_20200622_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeuresTravail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lundi_ouverture', models.TimeField(blank=True, default=datetime.datetime(2020, 6, 25, 22, 15, 2, 375980, tzinfo=utc), null=True)),
                ('Lundi_cloture', models.TimeField(blank=True, default=datetime.datetime(2020, 6, 25, 22, 15, 2, 375980, tzinfo=utc), null=True)),
                ('Mardi_ouverture', models.TimeField(blank=True, default=datetime.datetime(2020, 6, 25, 22, 15, 2, 375980, tzinfo=utc), null=True)),
                ('Mardi_cloture', models.TimeField(blank=True, default=datetime.datetime(2020, 6, 25, 22, 15, 2, 375980, tzinfo=utc), null=True)),
                ('Mercredi_ouverture', models.TimeField(blank=True, default=datetime.datetime(2020, 6, 25, 22, 15, 2, 375980, tzinfo=utc), null=True)),
                ('Mercredi_cloture', models.TimeField(blank=True, default=datetime.datetime(2020, 6, 25, 22, 15, 2, 375980, tzinfo=utc), null=True)),
                ('Jeudi_ouverture', models.TimeField(blank=True, default=datetime.datetime(2020, 6, 25, 22, 15, 2, 375980, tzinfo=utc), null=True)),
                ('Jeudi_cloture', models.TimeField(blank=True, default=datetime.datetime(2020, 6, 25, 22, 15, 2, 375980, tzinfo=utc), null=True)),
                ('Vendredi_ouverture', models.TimeField(blank=True, default=datetime.datetime(2020, 6, 25, 22, 15, 2, 375980, tzinfo=utc), null=True)),
                ('Vendredi_cloture', models.TimeField(blank=True, default=datetime.datetime(2020, 6, 25, 22, 15, 2, 375980, tzinfo=utc), null=True)),
                ('Samedi_ouverture', models.TimeField(blank=True, default=datetime.datetime(2020, 6, 25, 22, 15, 2, 375980, tzinfo=utc), null=True)),
                ('Samedi_cloture', models.TimeField(blank=True, default=datetime.datetime(2020, 6, 25, 22, 15, 2, 375980, tzinfo=utc), null=True)),
                ('Dimanche_ouverture', models.TimeField(blank=True, default=datetime.datetime(2020, 6, 25, 22, 15, 2, 375980, tzinfo=utc), null=True)),
                ('Dimanche_cloture', models.TimeField(blank=True, default=datetime.datetime(2020, 6, 25, 22, 15, 2, 375980, tzinfo=utc), null=True)),
            ],
        ),
        migrations.AddField(
            model_name='restau',
            name='HeuresTrv',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='HeuresTrv', to='list.HeuresTravail'),
        ),
    ]
