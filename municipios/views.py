from django.shortcuts import render

def inicio(request):
    return render(request, 'municipios/inicio.html')
# Create your views here.
