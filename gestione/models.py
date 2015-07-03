from django.db import models

class Persona(models.Model):
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)
    matricola = models.CharField(max_length=10,primary_key=True)
    def __unicode__(self):
        return self.cognome+' '+self.nome