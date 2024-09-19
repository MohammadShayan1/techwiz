from django.urls import path
from . import views

urlpatterns = [
    path('weather_data/', views.record_weather_data, name='weather_data'),
    path('', views.display_weather_data, name='display_weather_data'),
]
