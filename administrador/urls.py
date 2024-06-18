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

    path('crud_juegos_pc',views.crud_juegos_pc, name='crud_juegos_pc'),
    path('juegos_pc_add',views.juegos_pc_add ,name='juegos_pc_add'),
    path('juegos_pc_del/<str:pk>', views.juegos_pc_del, name='juegos_pc_del'),
    path('juegos_pc_edit/<str:pk>', views.juegos_pc_edit, name='juegos_pc_edit'),

    path('crud_juegos_ps5',views.crud_juegos_ps5, name='crud_juegos_ps5'),
    path('juegos_ps5_add',views.juegos_ps5_add ,name='juegos_ps5_add'),
    path('juegos_ps5_del/<str:pk>', views.juegos_ps5_del, name='juegos_ps5_del'),
    path('juegos_ps5_edit/<str:pk>', views.juegos_ps5_edit, name='juegos_ps5_edit'),

    path('crud_juegos_ps4',views.crud_juegos_ps4, name='crud_juegos_ps4'),
    path('juegos_ps4_add',views.juegos_ps4_add ,name='juegos_ps4_add'),
    path('juegos_ps4_del/<str:pk>', views.juegos_ps4_del, name='juegos_ps4_del'),
    path('juegos_ps4_edit/<str:pk>', views.juegos_ps4_edit, name='juegos_ps4_edit'),
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)