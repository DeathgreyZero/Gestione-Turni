import sqlite3
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

a = c.execute("SELECT * FROM gestione_persona")
nome = []
for course in a.fetchall():
    nome.append("{0}".format(course[0]))

print nome

c.close()