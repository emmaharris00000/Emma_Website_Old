from django.urls import path
from . import views

urlpatterns = [
    path ('home', views.home, name = "home"),
    path ("cv", views.cv, name = "cv"),
    path ("contact", views.contact, name = "contact"),
    path ("art", views.art, name = "art"),
]
