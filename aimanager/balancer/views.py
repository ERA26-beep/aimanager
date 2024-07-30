from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .forms import UploadDatasetForm, UploadAIModelForm
from .models import UploadDataset

menu = [
    {'title': 'Хранилище', 'url_name': 'storage'},
    {'title': 'Балансировщик нагрузки', 'url_name': 'balance'},
    {'title': 'Загрузка Датасетов', 'url_name': 'upload_dataset'},
    {'title': 'Загрузка ИИ моделей', 'url_name': 'upload_ai_model'}
]


def upload_dataset(request):
    if request.method == 'POST':
        form = UploadDatasetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_dataset')
    else:
        form = UploadDatasetForm()

    data = {
        'title': 'Загрузка Датасетов',
        'menu': menu,
        'form': form,
    }
    return render(request, 'balancer/upload_dataset.html', data)


def upload_ai_model(request):
    if request.method == 'POST':
        form = UploadAIModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_ai_model')
    else:
        form = UploadAIModelForm()

    data = {
        'title': 'Загрузка ИИ моделей',
        'menu': menu,
        'form': form,
    }
    return render(request, 'balancer/upload_ai_model.html', data)


def storage(request):

    data = {
        'title': 'Главная страница storage',
        'menu': menu,
    }
    return render(request,
                  'balancer/storage.html',
                  data,)


def load_balancer(request):
    data = {
        'title': 'Страница load_balancer',
        'menu': menu,
    }
    return render(request,
                  'balancer/load_balancer.html',
                  data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена<h1>")
