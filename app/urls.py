"""TweetTrend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    #path('trend/', views.trend, name='trend'),
    #path('trend/', views.trend.as_view(), name='trend'),
    #path('trend/forms/', views.trend_forms, name='trend_forms'),
    path('trend/', views.trend_forms,  name='trend'),
    path('<int:trend_id>/tweet/', views.tweet, name='tweet'),
    path('<int:trend_id>/trendurl/', views.trendurl, name='trendurl'),
]
