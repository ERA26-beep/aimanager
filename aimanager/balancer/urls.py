from django.urls import path
from . import views

urlpatterns = [
    path('', views.storage, name='storage'),  # http://127.0.0.1:8000/
    path('balance/', views.load_balancer, name='balance'),  # http://127.0.0.1:8000/storage/
    path('upload_dataset/', views.upload_dataset, name='upload_dataset'),  # http://127.0.0.1:8000/upload_dataset/
    path('upload_ai_model/', views.upload_ai_model, name='upload_ai_model'),  # http://127.0.0.1:8000/upload_ai_model/
]
