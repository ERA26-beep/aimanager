from django import forms

from .models import UploadDataset, UploadAIModel


class UploadDatasetForm(forms.ModelForm):
    class Meta:
        model = UploadDataset
        fields = ['name', 'file']


class UploadAIModelForm(forms.ModelForm):
    class Meta:
        model = UploadAIModel
        fields = ['name', 'file']