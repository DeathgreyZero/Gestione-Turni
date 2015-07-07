from django.db import models

class Persona(models.Model):
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)
    matricola = models.CharField(max_length=10,primary_key=True)
    anno_freq = models.IntegerField()
    ultimo_turno = models.IntegerField()
    riposo = models.IntegerField()
    count_giorno = models.IntegerField()
    def __unicode__(self):
        return self.cognome+' '+self.nome+' Mat. '+self.matricola



