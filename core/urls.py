
from django.contrib import admin
from django.urls import path, include  # Importando 'include' para incluir outras URLs
from api.urls import api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)), 
]
