from django.contrib import admin
from .models import Persona
# Register your models here.


class PersonaAdmin(admin.ModelAdmin):
    exclude = ['ultimo_turno','riposo']

admin.site.register(Persona,PersonaAdmin)