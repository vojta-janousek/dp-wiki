from django.urls import path

from wiki import views


urlpatterns = [
    path('', views.home, name='home')
]
