from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^buscaEspProf/', views.buscaEspProf, name='buscEspProf'),
    url(r'^listaProfesionales/', views.listaProfesionales, name='listaProfesionales'),

]