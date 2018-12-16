import json
from django.http import HttpResponse
from django.shortcuts import render
from apps.core.models import Especialidad, Persona, DatosProfesionales
from apps.core.forms import BuscaEspProfForm

def index(request):
    mensaje = ''
    form = BuscaEspProfForm()
    if request.method == 'POST':
        form = BuscaEspProfForm(request.POST)
        if form.is_valid():
            palabra = form.cleaned_data['buscaEspProf'].upper()
            if palabra[:].find(', ') != -1:
                palabras = palabra.split(', ')
                apellido = palabras[0]
                nombre = palabras[1]
                profesionales = Persona.objects.filter(nombre=nombre).filter(apellido=apellido).filter(datos_profesionales__isnull=False)
            else:
                try:
                    especialidad = Especialidad.objects.get(descripcion=palabra)
                    datosPro = DatosProfesionales.objects.filter(especialidad=especialidad)
                    profesionales = []
                    for dato in datosPro:
                        if len(dato.personas.all()) > 0:
                            profesionales.append(dato.personas.all()[0])
                except Especialidad.DoesNotExist:
                    profesionales = None
            form = BuscaEspProfForm()
            if not profesionales:
                mensaje = "No existen resultados para la busqueda seleccionada."
            values= {
                'palabra':palabra,
                'form': form,
                'profesionales':profesionales,
                'mensaje':mensaje,
            }
            return render(request, 'index.html', values)
    values = {
        'form':form,
        'mensaje':mensaje,
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


