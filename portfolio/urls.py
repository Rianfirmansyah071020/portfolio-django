"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from portfolio.services import home


urlpatterns = [
    path('', home.index,  name='home'),
    path('profil_api', home.profil, name='profil_api_url'),
    path('profesi_api', home.profesi, name='profesi_api_url'),
    path('skill_api', home.skill, name='skill_api_url'),
    path('pendidikan_api', home.pendidikan, name='pendidikan_api_url'),
    path('pengalaman_api', home.pengalaman, name='pengalaman_api_url'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Tambahkan ini hanya saat DEBUG = True
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)