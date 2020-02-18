from django.urls import path
from .views import NoticiaDetail

urlpatterns = [
    # path('/<int:pk>/', NoticiaDetail, name='detalle-noticia'),
    path('', NoticiaDetail, name='detalle-noticia'),
]
