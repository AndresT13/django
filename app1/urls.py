"""app1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.http import HttpResponse
from app1 import views as local_views


# Módulo hoteles
from hotels import views  as hotels_view


def test(request):
    return HttpResponse('Soy nivel Pro')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test),
    path('testUno/', local_views.testUno),
    path('test3/', local_views.test3),
    path('test4/<str:name>/<str:country>', local_views.test4),
    path('hotels',hotels_view.list_hotels)

]
