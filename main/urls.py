from django.urls import path
from . import views

urlpatterns = [
    path('history',views.index),
    path('', views.home),
    path('about',views.about),
    path('future',views.future),
    path('registery',views.registery),
    path('auth',views.authkod),

]


