from django.shortcuts import render, redirect

from apps.core.models import CentroMedico



def admin_home(request):
    titulo = "ADMIN_HOME:HTML"
    values={
        'titulo':titulo
    }
    return render(request, 'admin_home.html', values)

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
    return render(request, 'admin_home.html', values)

def centroMedico_alta(request):
    pass

def centroMedico_baja(request):
    pass

def centroMedico_modificacion(request):
    pass

def centroMedico_detalle(request):
    pass