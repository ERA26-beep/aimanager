from django.contrib import admin
from .models import UploadDataset, UploadAIModel

admin.site.register(UploadDataset)
admin.site.register(UploadAIModel)
