import calendar
from array_persona import *
import numpy


def cordinate(row, col):
    return (row + col) + (row * 6)

lista_notti_effettuate = []
#notti = 'Lunedi,Martedi,'
def get_notti(notti):
    j = 0
    for i in range(0,len(notti)):
        if notti[i] == ',':
            lista_notti_effettuate.append(notti[j:i])
            j = i+1



cal = calendar.Calendar()
year = 2015
month = 12
festivi = []

if month == 12:
    festivi = [25,26]
if month == 1:
    festivi = [1,6]

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


def calcola_turno(reparto,days,n_days):
    nome = ''
    print days

    for count in xrange(1,len(persone)+1):
        p = Persona.objects.get(pk = persone[count-1].matricola)
        print 'Seleziono -> : '+p.nome
        get_notti(p.nomi_notti_effettuate)
        print ">>>>>>>>>>>>> FUNZIONE GET_NOTTI<<<<<<<<<<<"
        print lista_notti_effettuate
        if (((((((days == 'Sabato' or days == 'Domenica' or n_days in festivi) or reparto%2 == 0) and p.indice_preso == 0) and p.indice_notte <= 1)and p.maternita == 0)) and ((p.turni_effettuati < 4 and (p.anno_freq > 3 or p.max_turni_mese_prec == 1))or(p.turni_effettuati<5 and (p.anno_freq < 4 and p.max_turni_mese_prec == 0)))):
            if reparto ==  1 and p.anno_freq <= 2:
                p.turni_effettuati +=1
                if p.turni_effettuati == 5:
                    p.max_turni_mese_prec = 1
                p.indice_preso = 1
                p.save()
                print 'Idoneo, prendo '+p.nome
                return p.nome
            if (reparto == 2 and p.indice_notte == 0) and ((days != 'Martedi' and days not in lista_notti_effettuate) or (days == 'Martedi' and p.martedi_notte < 2)):
                print 'indice notti : '+str(p.indice_notte)
                if days == 'Martedi':
                    p.martedi_notte +=1
                temp = p.nomi_notti_effettuate+days+','
                p.nomi_notti_effettuate = temp
                p.numero_notti +=1
                p.turni_effettuati +=1
                if p.turni_effettuati == 5:
                    p.max_turni_mese_prec = 1
                p.indice_preso = 1
                p.indice_notte = 3
                p.save()
                print 'Idoneo, prendo '+p.nome
                return p.nome
            if reparto == 3 and p.anno_freq >=3:
                p.turni_effettuati+=1
                if p.turni_effettuati == 5:
                    p.max_turni_mese_prec = 1
                p.indice_preso = 1
                p.save()
                print 'Idoneo, prendo '+p.nome
                return p.nome
            if ((reparto == 4 and p.abilitazione_neo == 1) and p.indice_notte == 0) and ((days != 'Martedi' and days not in lista_notti_effettuate) or (days == 'Martedi' and p.martedi_notte < 2)):
                print 'indice notti : '+str(p.indice_notte)
                if days == 'Martedi':
                    p.martedi_notte +=1
                temp = p.nomi_notti_effettuate+days+','
                p.nomi_notti_effettuate = temp
                p.numero_notti +=1
                p.turni_effettuati +=1
                if p.turni_effettuati == 5:
                    p.max_turni_mese_prec = 1
                p.indice_preso = 1
                p.indice_notte = 3
                p.save()
                print 'Idoneo, prendo '+p.nome
                return p.nome
            if reparto == 5:
                p.turni_effettuati+=1
                if p.turni_effettuati == 5:
                    p.max_turni_mese_prec = 1
                p.indice_preso = 1
                p.save()
                print 'Idoneo, prendo '+p.nome
                return p.nome
            if ((reparto == 6 and p.anno_freq >= 4) and p.indice_notte == 0) and ((days != 'Martedi' and days not in lista_notti_effettuate) or (days == 'Martedi' and p.martedi_notte < 2)):
                print 'indice notti : '+str(p.indice_notte)
                if days == 'Martedi':
                    p.martedi_notte +=1
                temp = p.nomi_notti_effettuate+days+','
                p.nomi_notti_effettuate = temp
                p.numero_notti +=1
                p.turni_effettuati +=1
                if p.turni_effettuati == 5:
                    p.max_turni_mese_prec = 1
                p.indice_preso = 1
                p.indice_notte = 3
                p.save()
                print 'Idoneo, prendo '+p.nome
                return p.nome
            print p.nome+' NON E IDONEO'
        print 'NESSUNO E IDONEO'
        if p.indice_preso > 0 and reparto == 1:
            p.indice_preso = 0
            p.save()
        #indice_notte deve essere decrementato dopo che passa un giorno
        if p.indice_notte > 0 and reparto == 1:
            p.indice_notte -=1
            p.save()
        continue
    return nome





counter = 1

for days in tupla4:
    mat.put(cordinate(counter-1, 0),str(counter)+' '+str(days))
    table = table + '<td class = "tg-031e">'+mat[counter-1][0]+'</td>'
    print '>>>>>>>>>>>>>>GIORNO '+str(counter)+'<<<<<<<<<<<<<<<<<<<<<'
    for reparto in range(1,7):
        print '>>>>>>>>>>>>> REPARTO: '+str(reparto)+'<<<<<<<<<<<<<<<<'
        turno = calcola_turno(reparto,days,counter)
        table = table+'<td class="tg-vn4c">' + turno + '</td>'
        mat.put(cordinate(counter-1,reparto),turno)
    table = table + "</tr>"
    counter += 1

#print mat