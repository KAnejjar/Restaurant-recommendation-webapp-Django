# Generated by Django 2.1.5 on 2020-06-16 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plat',
            name='prix',
            field=models.IntegerField(),
        ),
    ]
