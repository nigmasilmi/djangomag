from django.urls import path
from .views import NoticiaDetail

urlpatterns = [
    path('<int:noticia_id>/', NoticiaDetail, name='noticia'),
    # path('', NoticiaDetail, name='noticia'),
]
