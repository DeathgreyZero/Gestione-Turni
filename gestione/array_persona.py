import sqlite3
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

a = c.execute("SELECT * FROM gestione_persona WHERE matricola = 73288")
nome = []
for course in a.fetchall():
    nome = "{0}".format(course[0])
    print nome
c.close()