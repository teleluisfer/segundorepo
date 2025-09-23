from django.urls import path,include
from . import views
from .views import contact_view
from rest_framework import routers 

router = routers.DefaultRouter()
router.register(r'consulta1',views.consulta1ViewSet)
router.register(r'detallevulnerabilidad',views.DetalleVulnerabilidadViewSet)
router.register(r'graficavulnerabilidadriesgos',views.GraficaVulnerabilidadesViewSet)


urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('', views.inicio, name='inicio'),
    path('hola', views.hola, name='hola'),
    path('agregar', views.agregar_gasto, name='agregar_gasto'),
    path('login/', views.sign_in, name='login'),
    path('', include(router.urls)),
]

