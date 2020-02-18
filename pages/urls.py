from django.urls import path, include
from . views import home, archive, category, aboutUs, contact, standard_post

urlpatterns = [
    path('', home, name='home'),
    path('archive/', archive, name='archive'),
    path('category/', category, name='category'),
    path('about/', aboutUs, name='about'),
    path('contact/', contact, name='contact'),
    path('standard/', standard_post, name='standard-post'),

]
