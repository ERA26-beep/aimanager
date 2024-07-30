# Generated by Django 5.0.7 on 2024-07-24 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balancer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aimodel',
            old_name='created_at',
            new_name='time_create',
        ),
        migrations.RenameField(
            model_name='dataset',
            old_name='created_at',
            new_name='time_create',
        ),
        migrations.AddField(
            model_name='aimodel',
            name='time_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='dataset',
            name='time_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
