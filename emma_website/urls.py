from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include("home.urls")),
    path('art/', include("art.urls")),
    path('cv/', include("cv.urls")),
    path('contact/', include("contact.urls")),
]