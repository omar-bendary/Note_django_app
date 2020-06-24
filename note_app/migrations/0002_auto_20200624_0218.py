# Generated by Django 3.0.7 on 2020-06-24 02:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('note_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='owner',
        ),
        migrations.AddField(
            model_name='note',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
