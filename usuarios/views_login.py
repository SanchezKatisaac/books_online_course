from django.shortcuts import render

def pagina_login(request):
    params = {}
    return render(request, "usuario/login.html", params)