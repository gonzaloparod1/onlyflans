from django.core.management.base import BaseCommand
from web.forms import ContactFormForm

class Command(BaseCommand):
    help = 'Test form creation and validation'

    def handle(self, *args, **options):
        self.function_test_form()

    def function_test_form(self):  
        miFormVacio = ContactFormForm()
        print(f'01: {miFormVacio}')
        
        miFormConInfo = ContactFormForm({"customer_email": "kiki@gamial.com", "customer_name": "Kiki", "message": "Hola soy Kiki"})
        print(f'02: {miFormConInfo}')
        print(f'03: {miFormConInfo.as_table}')
        print(f'0300: {miFormConInfo.as_table()}') #* EJECUTAMOS as_table
        
        is_valid = miFormConInfo.is_valid()
        print(f'04: {is_valid}')
        if is_valid:
            print(f'05: OK -> {miFormConInfo.cleaned_data}')
        else:
            print(f'05: ERROR -> {miFormConInfo.errors}')

#* ContactForm.objects.create(**form.cleaned_data) <- sintaxis simple y adecuada para crear en la db

#!IMPORTANTE al momento de crear en la db con la data que nos llega
#* Sin uso de **, debemos descomponer del diccionario todos los atributos cual argumentos:
"""
contact_form = ContactForm.objects.create(
    name=form.cleaned_data['name'],
    email=form.cleaned_data['email'],
    message=form.cleaned_data['message']
)
"""

