from django.urls import path

from wiki import views


app_name = 'wiki'
urlpatterns = [
    path('', views.home, name='home')
]
