from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flan, ContactForm
from .forms import ContactFormForm, ContactModelForm
from django.contrib.auth.decorators import login_required


def indice(request):
    # public_flans = [{"name": "flan 1", "image_url": "https://pbs.twimg.com/media/CA5u_1pWYAE6FK0.jpg", "description": "flan 1"}, {"name": "flan 2",                                                                                                                              "image_url": "https://pbs.twimg.com/media/CA5u_1pWYAE6FK0.jpg", "description": "flan 2"}, {"name": "flan 3", "image_url": "https://pbs.twimg.com/media/CA5u_1pWYAE6FK0.jpg", "description": "flan 3"}]
    # return render(request,'index.html',{'public_flans': public_flans})

    # flanes_all = Flan.objects.all()
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {
        "mensaje": "hola",
        "flanes_publicos": flanes_publicos,
    }
    return render(request, 'index.html', context)


def acerca(request):
    # *  <!-- apply filtros -->
    return render(request, 'about.html', {})

#* vista BIENVENIDO es similar a la vista INDEX - pero muestra solo los flanes privados

@login_required
def bienvenido(request):
    # private_flans = [{"name": "flan 7", "image_url": "https://pbs.twimg.com/media/CA5u_1pWYAE6FK0.jpg", "description": "flan 7"},
    #                  {"name": "flan 8", "image_url": "https://pbs.twimg.com/media/CA5u_1pWYAE6FK0.jpg", "description": "flan 8"},]
    # return render(request,'welcome.html',{'private_flans': private_flans})
    private_flans = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {"private_flans": private_flans})

# *  <!-- apply FORM contacto -->


def contacto(request):
    if request.method == 'POST':
        
        #* FORM
        form = ContactFormForm(request.POST) # <- {"customer_email": "kiki@gamial.com", "customer_name": "Kiki", "message": "Hola soy Kiki"}
        print(f'errors -> {form.errors}')
        if form.is_valid():
            #* MODEL - Guardamos la data en nuestra DB en la TABLA CONACTFORM
            ContactForm.objects.create(**form.cleaned_data) # pasamos la data del diccionario .cleaned_data a argumentos
            return HttpResponseRedirect('/exito')
    else: 
        form = ContactFormForm()   
    return render(request, 'contactus.html', {'form':form})


# *  --- apply ContactModelForm ---
# from .forms import ContactModelForm  # Asegúrate de importar el formulario correcto

# *  <!-- apply MODEL-FORM contacto -->
def contacto_model_form(request):
    return render(request, 'contactus_model_form.html', {})
# *  --- apply ContactModelForm ---


# * <!-- apply DAY 11 - 12 -->
def exito(request):
    return render(request, 'success.html', {})


def nueva_vista(req):
    context = {
        "username": "Mauricio",
        "age": 33
    }
    return render(req, 'nueva_vista.html', context)

def detalle_flan(request, flan_uuid):
    flan = Flan.objects.get(flan_uuid = flan_uuid)
    return render(request, 'detail_flan.html', {'flan' : flan})


# def favorites(request):
#     return render(request, 'favorite.html', {})

        # pepe = ContactFormForm()
        # pepe.cleaned_data #    -> {"customer_email": "", "customer_name": "", "message": ""}
        # juncito = ContactFormForm({"customer_email": "ww@g.com", "customer_name": "www", "message": "zzz"})
        # juncito.cleaned_data #    -> {"customer_email": "ww@g.com", "customer_name": "www", "message": "zzz"}
        # juncito.is_valid() # -> True 
        # juncito.customer_email.error_messages
        # juncito.customer_email # -> <input ..... ...   value="ww@g.com" />
        # juncito.customer_name # -> <input ..... ...   value="www" />
        # juncito
"""
* juncito ->
<div>
    <label for="id_customer_email">Correo:</label>
    <input type="email" name="customer_email" value="ww@g.com" maxlength="320" required id="id_customer_email">
</div>
<div>
    <label for="id_customer_name">Nombre:</label>
    <input type="text" name="customer_name" value="www" maxlength="64" required id="id_customer_name">
</div>
<div>
    <label for="id_message">Mensaje:</label>
    <input type="text" name="message" value="zzz" required id="id_message">
</div>
"""


@login_required
def crer_flan():
    pass