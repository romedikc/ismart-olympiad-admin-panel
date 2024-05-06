# Generated by Django 5.0.4 on 2024-05-06 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_team_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='team',
            name='is_arrived',
            field=models.BooleanField(default=False),
        ),
    ]