from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flan, ContactForm, Profile
from .forms import ContactFormForm, ContactModelForm, ProfileForm, UserForm, CustomUserCreationForm
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

#* PROFILE
@login_required
def profile_view(request):
    # Verificar que el User tiene un Perfil 
    user_id = request.user.id 
    
    user = request.user
    #* User de no tener un Profile, crea la relación
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user)
        profile = Profile.objects.get(user_id=user_id)
        print(f'user profile get -> {profile.__dict__}')
        
    #* ARMADO POST - crea (guarda en la tabla) - y redirect
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # Redirigir a la misma página después de guardar
            return redirect('/profile_exito')
    #* GET FORM - Creamos los forms con los datos de la DB de ese user
    else: 
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

def profile_exito(request):
    return render(request, 'profile_exito.html', {})

#* REGISTER
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() #* Se guarda el user en la DB
            login(request, user) #* Se logea
            return redirect('profile')  # Redirige a la vista de perfil u otra vista
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

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