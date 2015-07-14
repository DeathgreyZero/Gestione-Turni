import calendar
import datetime
from array_persona import *
import numpy
import xlwt

#1.Giorno Accettazione
#2.Notte Accettazione
#3.Giorno Neonatologia
#4.Notte Neonatologia
#5.Giorno Reparto
#6.Notte Reparto

def cordinate(row, col):
    return (row + col) + (row * 6)


#funzione che ritorna le liste
def get_liste(stringa,lista):
    j = 0
    for i in range(0,len(stringa)):
        if stringa[i] == ',':
            lista.append(stringa[j:i])
            j = i+1


def reset():
    for count in xrange(1,len(persone)+1):
        pers = Persona.objects.get(pk = persone[count-1].matricola)
        pers.turni_effettuati = 0
        pers.nomi_notti_effettuate = ' '
        pers.martedi_notte = 0
        pers.numero_notti = 0
        pers.save()
    print 'RESET'



def crea_liste(month, year):
    calendario = calendar.Calendar().itermonthdays(year, month)
    day = ['Lunedi', 'Martedi', 'Mercoledi', 'Giovedi', 'Venerdi', 'Sabato', 'Domenica']

    cont = 0
    tupla  = []
    tupla2 = []
    mese = str(month) + '/' + str(year)

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

    tupla  = None
    tupla2 = None

    #Inizializzo la matrice
    mat = numpy.chararray((len(tupla3), 7))
    mat = numpy.chararray(mat.shape, itemsize='40')
    mat[:] = ' '

    return [tupla4, mat, mese]


def calcola_turno(reparto, days, n_days, lista_notti_effettuate, festivi):
    nome = ''

    for count in xrange(1,len(persone)+1):
        p = Persona.objects.get(pk = persone[count-1].matricola)
        if p.disponibile == 0:
            continue
        #print 'Seleziono -> : '+p.nome
        get_liste(p.nomi_notti_effettuate,lista_notti_effettuate)
        #print ">>>>>>>>>>>>> FUNZIONE GET_NOTTI<<<<<<<<<<<"
        #print lista_notti_effettuate
        if ((((((((days == 'Sabato' or days == 'Domenica' or (n_days in festivi ))) or reparto%2 == 0) and p.indice_preso == 0) and p.indice_notte <= 1)and p.maternita == 0)) and ((p.turni_effettuati < 4 and (p.anno_freq > 3 or p.max_turni_mese_prec == 1))or(p.turni_effettuati<5 and (p.anno_freq < 4 and p.max_turni_mese_prec == 0)))) and (str(n_days) not in p.desiderati_x):
            if reparto == 1 and (p.anno_freq <= 2 and str(n_days) not in p.desiderati_g):
                p.turni_effettuati +=1
                if p.turni_effettuati == 5:
                    p.max_turni_mese_prec = 1
                p.indice_preso = 1
                p.save()
                #print 'Idoneo, prendo '+p.nome
                return p.matricola
            if (reparto == 2 and (p.indice_notte == 0 and str(n_days) not in p.desiderati_n)) and ((days != 'Martedi' and days not in lista_notti_effettuate) or (days == 'Martedi' and p.martedi_notte < 2)):
                #print 'indice notti : '+str(p.indice_notte)
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
                #print 'Idoneo, prendo '+p.nome
                return p.matricola
            if reparto == 3 and (p.anno_freq >=3 and str(n_days) not in p.desiderati_g):
                p.turni_effettuati+=1
                if p.turni_effettuati == 5:
                    p.max_turni_mese_prec = 1
                p.indice_preso = 1
                p.save()
                #print 'Idoneo, prendo '+p.nome
                return p.matricola
            if ((reparto == 4 and (p.abilitazione_neo == 1 and str(n_days) not in p.desiderati_n)) and p.indice_notte == 0) and ((days != 'Martedi' and days not in lista_notti_effettuate) or (days == 'Martedi' and p.martedi_notte < 2)):
                #print 'indice notti : '+str(p.indice_notte)
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
                #print 'Idoneo, prendo '+p.nome
                return p.matricola
            if reparto == 5 and str(n_days) not in p.desiderati_g:
                p.turni_effettuati+=1
                if p.turni_effettuati == 5:
                    p.max_turni_mese_prec = 1
                p.indice_preso = 1
                p.save()
                #print 'Idoneo, prendo '+p.nome
                return p.matricola
            if ((reparto == 6 and (p.anno_freq >= 4 and str(n_days) not in p.desiderati_x)) and p.indice_notte == 0) and ((days != 'Martedi' and days not in lista_notti_effettuate) or (days == 'Martedi' and p.martedi_notte < 2)):
                #print 'indice notti : '+str(p.indice_notte)
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
                #print 'Idoneo, prendo '+p.nome
                return p.matricola
            #print p.nome+' NON E IDONEO'
        #print 'NESSUNO E IDONEO'
        if p.indice_preso > 0 and reparto == 1:
            p.indice_preso = 0
            p.save()
        #indice_notte deve essere decrementato dopo che passa un giorno
        if p.indice_notte > 0 and reparto == 1:
            p.indice_notte -=1
            p.save()
        continue
    return nome



def gen_turno(table, tupla4, mat, lista_notti_effettuate, festivi, month):
    counter = 1
    for days in tupla4:
        mat.put(cordinate(counter-1, 0),str(counter)+' '+str(days))
        table = table + '<td class = "tg-031e">'+mat[counter-1][0]+'</td>'
        #print '>>>>>>>>>>>>>>GIORNO '+str(counter)+'<<<<<<<<<<<<<<<<<<<<<'
        for reparto in range(1,7):
            #print '>>>>>>>>>>>>> REPARTO: '+str(reparto)+'<<<<<<<<<<<<<<<<'
            turno = calcola_turno(reparto,days,counter, lista_notti_effettuate, festivi)
            table = table+'<td class="tg-vn4c">' + turno + '</td>'
            mat.put(cordinate(counter-1,reparto),turno)
        table = table + "</tr>"
        counter += 1
    numpy.save(str(month), mat)

    return table



def save_xls(response, mese, mat):
    wbook = xlwt.Workbook()
    sheet = wbook.add_sheet('my_sheet')

    sheet.write(0, 0, mese)
    sheet.write(0, 1, 'Giorno ACC')
    sheet.write(0, 2, 'Notte ACC')
    sheet.write(0, 3, 'Giorno NEO')
    sheet.write(0, 4, 'Notte NEO')
    sheet.write(0, 5, 'Giorno REPARTO')
    sheet.write(0, 6, 'Notte REPARTO')

    for i in range(0, mat.shape[0]):
        for j in range(0, mat.shape[1]):
            sheet.write(i+1, j, mat[i, j])

    return wbook.save(response)



def load_mat(user, table_personale, mese):
    mat = numpy.load(str(mese)+'.npy')
    for i in range(0, mat.shape[0]):
        table_personale = table_personale + '<td class = "tg-031e">'+mat[i][0]+'</td>'
        for j in range(1, mat.shape[1]):
            if str(user).upper() == str(mat[i,j]).upper():
                table_personale = table_personale+'<td class="tg-vn4c">'+str(user).upper()+'</td>'
            else:
                table_personale = table_personale+'<td class="tg-vn4c">'+' '+'</td>'
        table_personale = table_personale + "</tr>"
    return table_personale