"""
URL configuration for restapi project.

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


from django.urls import re_path, path
from django.contrib import admin
from django.urls import path
from api import views
from django.urls import re_path as url
from rest_framework.authtoken.views import obtain_auth_token





urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('register',views.register.as_view(),name='register'),
    path('login/',obtain_auth_token,name='login'),
]
