import json
from django.http import HttpResponse
from django.shortcuts import render
from apps.core.models import Especialidad, Persona
from apps.core.forms import BuscaEspProfForm



def index(request):
    form = BuscaEspProfForm()
    values = {
        'form':form,
    }
    return render(request, 'index.html', values)

def buscaEspProf(request):
    if request.is_ajax:
        palabra = request.GET.get('term','')
        especialidades = Especialidad.objects.filter(descripcion__icontains = palabra)
        profesionales = Persona.objects.filter(apellido__icontains = palabra, datos_profesionales__isnull = False) | Persona.objects.filter(nombre__icontains = palabra, datos_profesionales__isnull = False)
        results = []
        for especialidad in especialidades:
            especialidad_json = {}
            especialidad_json['label'] = especialidad.descripcion
            especialidad_json['value'] = especialidad.descripcion
            results.append(especialidad_json)
        for profesional in profesionales:
            profesional_json = {}
            profesional_json['label'] = profesional.apellido +", " +profesional.nombre
            profesional_json['value'] = profesional.apellido +", " +profesional.nombre
            results.append(profesional_json)
        data_json = json.dumps(results)
    else:
        data_json = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data_json, mimetype)

def listaProfesionales(request, palabra):
    pass
