from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_usuario, name='login'),
    path('registro/', views.registro_escuela, name='registro'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.cerrar_sesion, name='logout'),
]
