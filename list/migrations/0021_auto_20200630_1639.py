# Generated by Django 2.2 on 2020-06-30 14:39

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0020_auto_20200630_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Likes', models.IntegerField(default=0)),
                ('Contenu', models.TextField()),
                ('Date_pub', models.DateTimeField(blank=True, null=True)),
                ('Restau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.Restau')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.User')),
            ],
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Dimanche_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 30, 14, 39, 5, 986972, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Dimanche_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 30, 14, 39, 5, 986972, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Jeudi_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 30, 14, 39, 5, 986972, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Jeudi_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 30, 14, 39, 5, 986972, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Lundi_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 30, 14, 39, 5, 986972, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Lundi_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 30, 14, 39, 5, 986972, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Mardi_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 30, 14, 39, 5, 986972, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Mardi_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 30, 14, 39, 5, 986972, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Mercredi_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 30, 14, 39, 5, 986972, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Mercredi_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 30, 14, 39, 5, 986972, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Samedi_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 30, 14, 39, 5, 986972, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Samedi_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 30, 14, 39, 5, 986972, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Vendredi_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 30, 14, 39, 5, 986972, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Vendredi_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 6, 30, 14, 39, 5, 986972, tzinfo=utc), null=True),
        ),
        migrations.CreateModel(
            name='Reponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Likes', models.IntegerField(default=0)),
                ('Contenu', models.TextField()),
                ('Date_pub', models.DateTimeField(blank=True, null=True)),
                ('Com', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.Commentaire')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.User')),
            ],
        ),
    ]
