from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('index',views.index, name='index'),
    
    path('ps5',views.ps5, name='ps5'),
    path('ps4',views.ps4, name='ps4'),
    path('pc',views.pc, name='pc'),
    path('crearc',views.crearc, name='crearc'),
    path('registro',views.registro, name='registro'),
    path('carrito/', views.carrito, name='carrito'),
    path('carrito_add/<str:correo>/<str:idjuego>', views.carrito_add, name='carrito_add'),
    path('carrito_del/<str:correo>/<str:idjuego>', views.carrito_del, name='carrito_del'),
    path('game/<str:idjuego>',views.game, name='game'),
    
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)