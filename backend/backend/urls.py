"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('search/', TemplateView.as_view(template_name='index.html')),
    path('upload/', TemplateView.as_view(template_name='index.html')),
    path('document/', TemplateView.as_view(template_name='index.html')),
    path('dashboard/',TemplateView.as_view(template_name='index.html')),
    # path('user/', include('user.urls')),
    path('data/', include('data.urls')),
    path('block/', include('block.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
