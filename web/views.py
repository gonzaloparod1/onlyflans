from django.shortcuts import render

# Create your views here.
def bienvenido(req):
    context = {
        "data": "Bienvenido a Only-Flans"
    }
    return render(req, 'welcome.html', context)

def acerca(req):
    contex = {
        "data": "Acerca de nosotros"
    }
    return render(req, 'about.html', contex)




