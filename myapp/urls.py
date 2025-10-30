from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.upload_create, name="upload_create"),
    path("uploads/", views.upload_list, name="upload_list"),
]
