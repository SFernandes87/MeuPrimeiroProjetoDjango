"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from saf.views import home
from saf.views import safListarView  #Class Based Views
from saf.views import safCriarView

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", home),
    #path("", safListar),
    path("", safListarView.as_view(template_name="saf/saflistar.html")),
    path("criar", safCriarView.as_view(), name='saf_criar')   
]
