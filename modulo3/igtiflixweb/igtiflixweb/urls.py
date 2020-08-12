from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('principal/', view=include('principal.urls'))  # pasta: principal, arquivo: urls
]
