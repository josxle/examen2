from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomeViewList.as_view(), name='home'),
    path('crear/', Create.as_view(), name="create"),
    path('detalle/<int:pk>/', Detail.as_view(), name="detail"),
    path('editar/<int:pk>/', Update.as_view(), name="update"),
    path('eliminar/<int:pk>/', Delete.as_view(), name="delete"),
]

