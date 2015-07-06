import calendar
import array_persona
import numpy


def cordinate(row, col):
    return (row + col) + (row * 6)

cal = calendar.Calendar()
year = 2015
month = 9
calendario = cal.itermonthdays(year, month)
day = ['Lunedi', 'Martedi', 'Mercoledi', 'Giovedi', 'Venerdi', 'Sabato', 'Domenica']
cont = 0
tupla = []
tupla2 = []

for i in calendario:
    tupla.append(i)
    tupla2.append(day[cont % len(day)])
    cont += 1

tupla3 = []
tupla4 = []

for i in xrange(0, len(tupla)):
    if tupla[i] != 0:
        tupla3.append(tupla[i])
        tupla4.append(tupla2[i])

tupla = None
tupla2 = None
mese = str(month) + '/' + str(year)

table = """<table class="tg">
  <tr>
    <th class="tg-031e">""" + mese + """</th>
    <th class="tg-031e">Giorno ACC</th>
    <th class="tg-031e">Notte ACC</th>
    <th class="tg-031e">Giorno NEO</th>
    <th class="tg-031e">Notte NEO</th>
    <th class="tg-031e">Giorno REPARTO</th>
    <th class="tg-031e">Notte REPARTO</th>
  </tr>
  <tr>
"""

mat = numpy.chararray((len(tupla3), 7))
mat = numpy.chararray(mat.shape, itemsize='40')
mat[:] = ' '
#mat.put(cordinate(1, 6), 'ciao')
# print mat


def calcola_turno(reparto):
    nome = ''
    if reparto == 1:
        nome = 'Giovanni'
    if reparto == 3:
        nome = 'Luca'
    return nome

#1.Giorno Accettazione
#2.Notte Accettazione
#3.Giorno Neonatologia
#4.Notte Neonatologia
#5.Giorno Reparto
#6.Notte Reparto

counter = 1
for days in tupla4:
    mat.put(cordinate(counter-1, 0),str(counter)+' '+str(days))
    table = table + '<td class = "tg-031e">'+mat[counter-1][0]+'</td>'
    for reparto in range(1,7):
        turno = calcola_turno(reparto)
        table = table+'<td class="tg-vn4c">' + turno + '</td>'
        mat.put(cordinate(counter-1,reparto),turno)

    #table = table + '<td class="tg-031e">' + str(counter) + " " + str(days) + '</td>'
    #for i in array_persona.nome:
    #    table = table + '<td class="tg-vn4c">' + i + '</td>'
    table = table + "</tr>"
    counter += 1

print mat