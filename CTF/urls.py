"""CTF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import app.views as views
from django.conf.urls import url


urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$',views.index),
    url(r'^login/',views.custom_login),
    url(r'^register/',views.register),
    url(r'^leaderboard/',views.leaderboard),
    url(r'^challenges/',views.challenges),
    url(r'^aboutus/',views.about_us),
    url(r'^logout/',views.custom_logout),
    url(r'^rules/',views.rules),
    url(r'^uservalidator/',views.validate_username),
    # url(r'timer/',views.timer),

]
