"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path , include 
from django.conf import settings
from django.conf.urls.static import static
from polls.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('Courses/',Courses_ , name='Courses'),
    path('Courses/<int:id>',Courses_single , name='Course'),

    path('Blogs/', Blogs_ , name='Blogs'),
    path('Blog/<int:id>', single_blog , name='Blog'),

    path('Contact/', contact_ , name='contact'),
    path('',Home , name='home'),
]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)