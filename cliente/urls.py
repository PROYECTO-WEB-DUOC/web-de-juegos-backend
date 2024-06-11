from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('index',views.index, name='index'),
    path('crud', views.crud, name='crud'),
    path('clientesAdd', views.clientesAdd, name='clientesAdd'),
    path('gow',views.gow, name='gow'),
    path('spider',views.spider, name='spider'),
    path('bloodborne',views.bloodborne, name='bloodborne'),
    path('dmc',views.dmc, name='dmc'),
    path('ps5',views.ps5, name='ps5'),
    path('ps4',views.ps4, name='ps4'),
    path('pc',views.pc, name='pc'),
    path('crearc',views.crearc, name='crearc'),
    path('registro',views.registro, name='registro'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)