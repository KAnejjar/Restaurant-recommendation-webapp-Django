# Generated by Django 2.1.5 on 2020-06-18 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0005_auto_20200618_0117'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeuresTravail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lundi_ouverture', models.DateTimeField()),
                ('Lundi_cloture', models.DateTimeField()),
                ('Mardi_ouverture', models.DateTimeField()),
                ('Mardi_cloture', models.DateTimeField()),
                ('Mercredi_ouverture', models.DateTimeField()),
                ('Mercredi_cloture', models.DateTimeField()),
                ('Jeudi_ouverture', models.DateTimeField()),
                ('Jeudi_cloture', models.DateTimeField()),
                ('Vendredi_ouverture', models.DateTimeField()),
                ('Vendredi_cloture', models.DateTimeField()),
                ('Samedi_ouverture', models.DateTimeField()),
                ('Samedi_cloture', models.DateTimeField()),
                ('Dimanche_ouverture', models.DateTimeField()),
                ('Dimanche_cloture', models.DateTimeField()),
            ],
        ),
    ]
