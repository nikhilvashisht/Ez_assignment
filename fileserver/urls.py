from django.urls import path
from fileserver import views

urlpatterns = [
    path('login', views.login),
    path('register', views.register),
    path('upload', views.upload_file),
    path('get', views.get_file),
    path('download/<str:file_id>', views.download_file)
]