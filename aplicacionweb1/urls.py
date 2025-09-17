from django.urls import path
from . import views
from .views import contact_view


#urlpatterns = [
#    path('post_list', views.post_list, name='post_list'),
#]


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('hola', views.hola, name='hola'),
    path('agregar', views.agregar_gasto, name='agregar_gasto'),
]

#urlpatterns = [
#    path('', views.post_list, name='post_list'),
#    path('post/<int:pk>/', views.post_detail, name='post_detail'),
#    path('post/new/', views.post_new, name='post_new'),
#]

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
]

#urlpatterns = [
#    path('people/', views.PersonCreateView, name='people'),
#]
