"""adressen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from adressverwaltung.views import home_page_view
from adressverwaltung.views import bearbeiten
from adressverwaltung.views import neu
from adressverwaltung.views import loeschen

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_page_view, name = "Homepage"),
    path("neu/", neu, name="neu"),
    path("<int:kunden_id>/", bearbeiten, name="bearbeiten"),
    path("<int:kunden_id>/loeschen/", loeschen, name="loeschen"),
]
