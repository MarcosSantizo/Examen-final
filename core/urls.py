from django.urls import path
from .views import home, creditos

urlpatterns = [
    path('', home, name='home'),
    path('creditos/', creditos, name='creditos'),
]
