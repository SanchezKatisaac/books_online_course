from django.shortcuts import render

def pagina_registro(request):
    params = {}
    return render(request, "usuario/registro.html", params)