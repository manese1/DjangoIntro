
from django.contrib import admin
from django.urls import path
from cartapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name = 'home'),
    path('gallery/', views.gallery, name = 'gallery'),
    path('services/', views.services, name = 'services')
]
