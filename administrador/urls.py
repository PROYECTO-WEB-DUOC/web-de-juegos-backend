from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin',views.admin, name='admin'),
    path('crud',views.crud, name='crud'),
    path('clientes_del/<str:pk>', views.clientes_del, name='clientes_del'),
    path('clientes_edit/<str:pk>', views.clientes_edit, name='clientes_edit'),
     
    path('crud_juegos',views.crud_juegos, name='crud_juegos'),
    path('juegos_add',views.juegos_add ,name='juegos_add'),
    path('juegos_del/<str:pk>', views.juegos_del, name='juegos_del'),
    path('juegos_edit/<str:pk>', views.juegos_edit, name='juegos_edit'),
    path('crud_carrito',views.crud_carrito, name='crud_carrito'),
    path('crud_carrusel',views.crud_carrusel, name='crud_carrusel'),
    path('carrusel_add',views.carrusel_add, name='carrusel_add'),
    path('carrusel_del/<str:nombre>',views.carrusel_del, name='carrusel_del'),
    path('carrusel_edit/<str:nombre>',views.carrusel_edit, name='carrusel_edit'),
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)