from django.db import models


class UploadDataset(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads_datasets')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)


class UploadAIModel(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads_ai_models')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
