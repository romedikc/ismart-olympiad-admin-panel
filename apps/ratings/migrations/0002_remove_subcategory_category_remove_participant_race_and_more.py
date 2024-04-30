# Generated by Django 5.0.4 on 2024-04-30 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='race',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='user',
        ),
        migrations.RemoveField(
            model_name='race',
            name='judges',
        ),
        migrations.RemoveField(
            model_name='race',
            name='subcategory',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Participant',
        ),
        migrations.DeleteModel(
            name='Race',
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
    ]
