from django.db import models

class Persona(models.Model):
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)
    matricola = models.CharField(max_length=10, primary_key=True,verbose_name='Codice Fiscale')
    anno_freq = models.IntegerField(default=1,help_text='Anno di Specializzazione (valori consentiti da 1 a 5)')
    maternita = models.IntegerField(default=0,help_text='1 per indicare la maternita\' 0 altrimenti')
    numero_notti = models.IntegerField(default=0)
    turni_effettuati = models.IntegerField(default=0)
    indice_preso = models.IntegerField(default=0)
    abilitazione_neo = models.IntegerField(default=0,help_text="1 per indicare che lo specializzando e' abilitato al reparto di Neonatologia, 0 altrimenti")
    indice_notte = models.IntegerField(default=0)
    nomi_notti_effettuate = models.CharField(max_length=500, default=' ')
    martedi_notte = models.IntegerField(default=0)
    max_turni_mese_prec = models.IntegerField(default=0,help_text='settare a 1 se lo specializzando ha fatto 5 turni nello scorso mese, 0 altrimenti')
    desiderati_x = models.CharField(default=' ', max_length=500,verbose_name='Giorni Desiderati Completi',help_text='Inserire i giorni desiderati seguiti da una virgola, ES.(24,25)')
    desiderati_g = models.CharField(default=' ', max_length=500,help_text='Inserire i giorni desiderati seguiti da una virgola, ES.(24,25)')
    desiderati_n = models.CharField(default=' ', max_length=500,help_text='Inserire i giorni desiderati seguiti da una virgola, ES.(24,25)')
    disponibile = models.IntegerField(default=1)

    def __unicode__(self):
        return self.cognome+' '+self.nome+' Mat. '+self.matricola




