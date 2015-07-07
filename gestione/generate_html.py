import calendar
from array_persona import *
import numpy


def cordinate(row, col):
    return (row + col) + (row * 6)

cal = calendar.Calendar()
year = 2015
month = 8
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



#1.Giorno Accettazione
#2.Notte Accettazione
#3.Giorno Neonatologia
#4.Notte Neonatologia
#5.Giorno Reparto
#6.Notte Reparto

numero_turni = 0
ultimo_turno = 0
def calcola_turno(reparto):
    nome = ''
    global ultimo_turno
    #ogni giorno diminuisce di 1 i contatori del riposo e del giorno
    print str(numero_turni)+'<<<<turni'
    if numero_turni%6 == 0:
        print ">>>>>>>>>>>>>>>>SCALO I RIPOSI<<<<<<<<<<<<<<<<<<<"
        query = Persona.objects.filter(count_giorno = 0)
        for count in xrange(1,len(persone)+1):
            r = Persona.objects.get(pk = persone[count-1].matricola)
            if r.count_giorno > 0 and not query:
                r.count_giorno -=1
                r.save()
            elif r.riposo <= 3 and r.riposo > 0:
                r.riposo -=1
                r.save()
            elif r.riposo == 0:
                r.ultimo_turno = 1
                r.save()

    for count in xrange(1,len(persone)+1):
        p = Persona.objects.get(pk = persone[count-1].matricola)
        print 'calcolo -> '+str(count)+' prendo: '+p.nome
        if p.riposo == 0:
            if reparto == 1:
                if p.count_giorno <= 1 and p.ultimo_turno%2 == 0:
                    nome = p.nome
                    p.count_giorno = 1
                    p.riposo = 1
                    p.ultimo_turno = 1
                    p.save()
                    print 'idoneo, salvo '+p.nome
                    return nome
                print 'non idoneo'
                print '1'
            elif reparto == 2:
                if p.count_giorno <= 1:
                    nome = p.nome
                    p.riposo = 3
                    p.ultimo_turno = 2
                    p.save()
                    print 'idoneo, salvo '+p.nome
                    return nome
                print 'non idoneo'
                print '2'
            elif reparto == 3:
                nome = '3'
            elif reparto == 4:
                nome = '4'
            elif reparto == 5:
                nome = '5'
            elif reparto == 6:
                nome = '6'
    return nome





counter = 1

for days in tupla4:
    mat.put(cordinate(counter-1, 0),str(counter)+' '+str(days))
    table = table + '<td class = "tg-031e">'+mat[counter-1][0]+'</td>'
    print '>>>>>>>>>>>>>>GIORNO '+str(counter)+'<<<<<<<<<<<<<<<<<<<<<'
    for reparto in range(1,7):
        print '>>>>>>>>>>>>> REPARTO: '+str(reparto)+'<<<<<<<<<<<<<<<<'
        turno = calcola_turno(reparto)
        table = table+'<td class="tg-vn4c">' + turno + '</td>'
        mat.put(cordinate(counter-1,reparto),turno)
        numero_turni +=1
    table = table + "</tr>"
    counter += 1

#print mat