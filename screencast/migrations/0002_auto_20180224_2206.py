# Generated by Django 2.0.2 on 2018-02-24 22:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('screencast', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 2, 24, 22, 6, 8, 576663, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='screencast',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 2, 24, 22, 6, 8, 577214, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subject',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 2, 24, 22, 6, 8, 576252, tzinfo=utc)),
        ),
    ]
