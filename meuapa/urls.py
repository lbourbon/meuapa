"""meuapa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from home.views import home, lista
from ficha.views import ficha, abrir_ficha, apagar_ficha, termo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista, name='lista'),
    path('lista/', lista, name='lista'),
    path('ficha/', ficha, name='ficha'),
    path('ler_ficha/<int:id>', abrir_ficha, name='ler_ficha'),
    path('apagar_ficha/<int:id>', apagar_ficha, name='apagar_ficha'),
    path('termo/<int:id>', termo, name='termo'),
]
