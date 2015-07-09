import sqlite3
from .models import Persona
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

a = c.execute("SELECT * FROM gestione_persona")
persone = []

for course in a.fetchall():
    persone.append(Persona(nome="{0}".format(course[0]),matricola="{0}".format(course[2]),anno_freq="{0}".format(course[3]),maternita="{0}".format(course[4]),
                           numero_notti = "{0}".format(course[5],turni_effettuati = "{0}".format(course[6]),
                           indice_preso = "{0}".format(course[7]),abilitazione_neo = "{0}".format(course[8]),
                           indice_notte = "{0}".format(course[9]),nomi_notti_effettuate = "{0}".format(course[10]),
                           martedi_notte = "{0}".format(course[11]))))

c.close()