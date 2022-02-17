# Generated by Django 4.0.1 on 2022-02-14 09:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='interest',
            new_name='client_needs',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='create_date',
        ),
        migrations.AddField(
            model_name='contact',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 14, 14, 43, 26, 852140)),
        ),
    ]