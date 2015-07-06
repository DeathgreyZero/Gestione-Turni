import sqlite3
from .models import Persona
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

a = c.execute("SELECT * FROM gestione_persona")
"""nome = []
anno = []
ultimo_turno = []
riposo = []"""
persone = []

for course in a.fetchall():
    """nome.append("{0}".format(course[0]))
    anno.append("{0}".format(course[3]))
    ultimo_turno.append("{0}".format(course[4]))
    riposo.append("{0}".format(course[5]))"""
    persone.append(Persona(nome="{0}".format(course[0]),matricola="{0}".format(course[2]),anno_freq="{0}".format(course[3]),ultimo_turno="{0}".format(course[4]),
                           riposo = "{0}".format(course[5])))
#print nome[0]+anno[0]

c.close()