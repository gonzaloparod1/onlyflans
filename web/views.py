from django.shortcuts import render

# Create your views here.

def inicio(req): 
    context = {
        "mensaje": "Bienvenido Cliente",
            }
    return render(req, 'index.html', context)

def acerca(req): 
    return render(req, 'about.html', {})