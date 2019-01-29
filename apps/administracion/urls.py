from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^admin_home/', views.admin_home, name='admin_home'),
    url(r'^centrosMedicos_lista/', views.centrosMedicos_lista, name='centrosMedicos_lista'),
    url(r'^centroMedico_alta/', views.centroMedico_alta, name='centroMedico_alta'),
    url(r'^centroMedico_baja/', views.centroMedico_baja, name='centroMedico_baja'),
    url(r'^centroMedico_modificacion/', views.centroMedico_modificacion, name='centroMedico_modificacion'),
    url(r'^centroMedico_detalle/', views.centroMedico_detalle, name='centroMedico_detalle'),
]
