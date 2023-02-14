from django.urls import path

from .views import get_index_page, get_place

urlpatterns = [
    path('', get_index_page),
    path('places/<int:place_id>', get_place, name='get_place'),
]
