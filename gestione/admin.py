from django.contrib import admin
from .models import Persona
# Register your models here.


class PersonaAdmin(admin.ModelAdmin):
    exclude = ['numero_notti','turni_effettuati','indice_preso','indice_notte','martedi_notte','nomi_notti_effettuate']

admin.site.register(Persona,PersonaAdmin)