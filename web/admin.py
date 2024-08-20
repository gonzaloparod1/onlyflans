from django.contrib import admin
from .models import Flan, ContactForm, Profile

admin.site.register(ContactForm)
admin.site.register(Flan)
admin.site.register(Profile)