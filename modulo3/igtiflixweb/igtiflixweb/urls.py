from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(route='principal/', view=include('principal.urls')),  # pasta: principal, arquivo: urls
    path(route='genero/', view=include('genero.urls'))
]
