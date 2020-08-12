from django.urls import path
from . import views  # . = diretório corrente


urlpatterns = [
    path('', views.index, name='index')  # arquivo: views, metodo: index
]