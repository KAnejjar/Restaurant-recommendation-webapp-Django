# Generated by Django 2.2 on 2020-07-01 23:03

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0013_auto_20200621_0426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentaire',
            name='Reponse',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Adresse',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Date_ajout',
        ),
        migrations.RemoveField(
            model_name='user',
            name='MotPasse',
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='static\\media'),
        ),
        migrations.AddField(
            model_name='user',
            name='sexe',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F')], default='M', max_length=2),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='Likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Dimanche_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 1, 23, 3, 10, 931673, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Dimanche_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 1, 23, 3, 10, 931673, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Jeudi_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 1, 23, 3, 10, 931673, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Jeudi_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 1, 23, 3, 10, 931673, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Lundi_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 1, 23, 3, 10, 931673, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Lundi_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 1, 23, 3, 10, 931673, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Mardi_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 1, 23, 3, 10, 931673, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Mardi_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 1, 23, 3, 10, 931673, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Mercredi_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 1, 23, 3, 10, 931673, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Mercredi_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 1, 23, 3, 10, 931673, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Samedi_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 1, 23, 3, 10, 931673, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Samedi_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 1, 23, 3, 10, 931673, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Vendredi_cloture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 1, 23, 3, 10, 931673, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='heurestravail',
            name='Vendredi_ouverture',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 7, 1, 23, 3, 10, 931673, tzinfo=utc), null=True),
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
