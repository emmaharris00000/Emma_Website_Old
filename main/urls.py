
from django.urls import path
from . import views

urlpatterns = [
    path ("", views.index, name = "home"),
    path ("", views.index, name = "about"),
    path ("", views.index, name = "cv"),
    path ("", views.index, name = "contact"),
    path ("", views.index, name = "art"),
    
]