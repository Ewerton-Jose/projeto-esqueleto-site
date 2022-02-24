from . import views
from django.urls import path

urlpatterns = [
    path('', views.inicio),
    path('produto/<int:id>', views.prodview),
]
