from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'jugadores', views.JugadorViewSet, basename='jugadores')

urlpatterns=[
    path('', include(router.urls)),

    path('jugadores/<int:jugador_id>/cartas/', views.CartaViewSet.as_view({'post': 'entregar_cartas'})),
    
    path('jugadores/<int:jugador_id>/cambio/', views.CartaViewSet.as_view({'post': 'cambiar_cartas'})),

    path('estado', views.PartidaViewSet.as_view({'get': 'estado'})),

    path('reiniciar', views.PartidaViewSet.as_view({'get': 'volverajugar'})),

    path('iniciar', views.PartidaViewSet.as_view({'get': 'iniciarjuego'}))
    
    
    ]