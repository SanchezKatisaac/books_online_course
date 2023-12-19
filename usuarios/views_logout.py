from django.shortcuts import render

def pagina_logout(request):
    params = {}
    return render(request, "usuario/logout.html", params)