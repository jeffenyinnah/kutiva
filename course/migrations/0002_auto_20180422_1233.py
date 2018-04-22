# Generated by Django 2.0.2 on 2018-04-22 12:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='subject',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='category',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='course',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='subject',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
