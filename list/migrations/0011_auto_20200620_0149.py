# Generated by Django 2.2 on 2020-06-19 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0010_auto_20200620_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='static\\media'),
        ),
    ]