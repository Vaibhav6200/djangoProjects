# Generated by Django 4.0.1 on 2022-01-25 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_team_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='created_date',
        ),
    ]