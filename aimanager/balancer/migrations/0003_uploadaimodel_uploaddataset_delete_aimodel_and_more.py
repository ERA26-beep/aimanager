# Generated by Django 5.0.7 on 2024-07-25 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balancer', '0002_rename_created_at_aimodel_time_create_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadAIModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='uploads_ai_models')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UploadDataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='uploads_datasets')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='AIModel',
        ),
        migrations.DeleteModel(
            name='Dataset',
        ),
    ]
