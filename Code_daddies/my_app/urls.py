from django.urls import path, include
from . import views


app_name = "my_app"

urlpatterns = [
    path('', views.home, name='home'),
    path('new_search/', views.new_search, name='new_search'),




]
