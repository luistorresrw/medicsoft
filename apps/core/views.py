from django.shortcuts import render

def index(request):
    mensaje = "Bienvenido a medicsoft"
    values = {
        'mensaje':mensaje,
    }
    return render(request, 'index.html', values)