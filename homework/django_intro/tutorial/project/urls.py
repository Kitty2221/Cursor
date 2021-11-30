
from django.urls import path

from .views import status_view
from .views import random_color

urlpatterns = [
    path('status/', status_view, name='status'),
    path('color/', random_color, name='color')
]