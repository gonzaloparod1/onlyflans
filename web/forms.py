from django import forms
from django.contrib.auth.models import User
from .models import ContactForm, Profile


# *  --- apply ContactFormForm ---

class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(label='Mensaje')

# *  --- apply ContactModelForm ---


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']

#* PROFILE FORMS 
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
# ---

"""
ContactForm que contenga los 
siguientes atributos:
● contact_form_uuid del tipo UUIDField, con valor por defecto uuid.uuid4, no 
editable
● customer_email del tipo EmailField
● customer_name del tipo CharField (largo máximo 64 caracteres)
● message del tipo TextField

pepe = ContactModelForm({"customer_email": "sasa",  "customer_name":"sisi", "message": "susu"})
pepe -> <label><input>  <label><input>  <label><input>  
<div>
    <label for="id_customer_email">Correo:</label>
    <input type="email" name="customer_email" value="sasa" maxlength="320" required id="id_customer_email">
</div>
<div>
    <label for="id_customer_name">Nombre:</label>
    <input type="text" name="customer_name" value="sisi" maxlength="64" required id="id_customer_name">
</div>
<div>
    <label for="id_message">Mensaje:</label>
    <input type="text" name="message" value="susu" required id="id_message">
</div>

pepe.customer_name -> <input type="text" name="customer_name" value="sisi" maxlength="64" required id="id_customer_name">

pepe.is_valid() -> False
pepe.cleaned_data -> {"customer_email": "sasa",  "customer_name":"sisi", "message": "susu"}
"""