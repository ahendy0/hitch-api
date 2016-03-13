"""HitchProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include 
from django.contrib import admin
from rest_framework import routers

from Rides.views import RideViewSet
from PersonApp.views import PersonViewSet
from Location.views import LocationViewSet



router = routers.DefaultRouter()

# router.register(r'person', PersonViewSet)
# router.register(r'location', LocationViewSet)
# router.register(r'ride', RideViewSet)



urlpatterns = [
	url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'persons', PersonViewSet.as_view()),
    url(r'location', LocationViewSet.as_view()),
    url(r'ride', RideViewSet.as_view()),


]
