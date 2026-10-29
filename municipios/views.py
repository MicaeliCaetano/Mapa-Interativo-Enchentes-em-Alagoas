from django.shortcuts import render

def inicio(request):
    return render(request, 'municipios/inicio.html', {
        'textos_municipios': render(
            request, 'municipios/municipio.html'
        ).content.decode('utf-8')
    })