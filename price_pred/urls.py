from django import views
from .views import predict
from django.urls import path
urlpatterns =  [
    path('', predict, name='predict'),

    path('predict/', predict, name='predict'),
]
                
