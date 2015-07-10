from django.db import models

class Persona(models.Model):
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)
    matricola = models.CharField(max_length=10,primary_key=True)
    anno_freq = models.IntegerField(default=1)
    maternita = models.IntegerField(default=0)
    numero_notti = models.IntegerField(default=0)
    turni_effettuati = models.IntegerField(default=0)
    indice_preso = models.IntegerField(default=0)
    abilitazione_neo = models.IntegerField(default=0)
    indice_notte = models.IntegerField(default=0)
    nomi_notti_effettuate = models.CharField(max_length=500,default=' ')
    martedi_notte = models.IntegerField(default=0)
    max_turni_mese_prec = models.IntegerField(default=0)
    def __unicode__(self):
        return self.cognome+' '+self.nome+' Mat. '+self.matricola



