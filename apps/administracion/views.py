from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext

from apps.core.models import CentroMedico



def admin_home(request):
    titulo = "ADMIN_HOME:HTML"
    values={
        'titulo':titulo
    }
    return render(request, 'admin_base.html', values)

def centrosMedicos_lista(request):
    titulo = 'CENTROS MEDICOS'
    thead = ['Centro Médico', 'Domicilio', 'Localidad']
    query = CentroMedico.objects.all()

    tbody = {}
    for item in query:
        tbody[item.id]='<td>'+ item.descripcion +'</td><td>'+ item.domicilio.all().order_by("-id")[0].direccion + '</td><td>'+str(item.domicilio.all().order_by("-id")[0].localidad)+'</td>'
    values = {
        'thead': thead,
        'titulo': titulo,
        'query': query,
        'tbody': tbody,
    }
    return render(request, 'abm.html', values)

def centroMedico_alta(request):
    pass

def centroMedico_baja(request):
    pass

def centroMedico_modificacion(request):
    pass

def centroMedico_detalle(request, centroMedico):
    titulo = 'CENTROS MEDICOS'
    clase = 'centroMedico'
    link_to_detalle = "{% url 'centroMedico_detalle' item.id %} "
    centroMedico = CentroMedico.objects.get(id=centroMedico)
    centroMedico_nombre = centroMedico.descripcion
    values = {
        'titulo': titulo,
        'clase': clase,
        'centroMedico': centroMedico,
        'centroMedico_nombre': centroMedico_nombre,
        'link_to_detalle': link_to_detalle,


    }
    return render(request, 'detalle.html', values)