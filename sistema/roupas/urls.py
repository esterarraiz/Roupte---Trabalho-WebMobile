from django.urls import path
from . import views
from roupas.views import Home, CriarAnuncio, FotoRoupa, DeletarAnuncio, EditarAnuncio

urlpatterns = [
    path('', Home.as_view(), name='principal'),
    path('novo/', CriarAnuncio.as_view(), name='criar-anuncio'),
    path('foto/<str:arquivo>/', FotoRoupa.as_view(), name='foto-roupa'),
    path('deletar/<int:pk>/', DeletarAnuncio.as_view(), name='deletar-anuncio'),
    path('editar/<int:pk>/', EditarAnuncio.as_view(), name='editar-anuncio'),
]