from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
import calendar
import array_persona
def index(request):
    print 'Index'
    return render(request,'gestione/index.html')



def stampa(request):
    print 'Sto Stampando'
    cal = calendar.Calendar()
    year = 2015
    month = 8
    calendario = cal.itermonthdays(year,month)
    day = ['Lunedi','Martedi','Mercoledi','Giovedi','Venerdi','Sabato','Domenica']
    cont = 0
    tupla = []
    tupla2 = []

    for i in calendario :
        tupla.append(i)
        tupla2.append(day[cont%len(day)])
        cont +=1

    tupla3 = []
    tupla4 = []

    for i in xrange(0,len(tupla)):
        if tupla[i] != 0:
            tupla3.append(tupla[i])
            tupla4.append(tupla2[i])

    tupla = None
    tupla2 = None
    return render(request,"gestione/stampa.html",{"tupla3":tupla3,"tupla4":tupla4,"array_persona":array_persona.nome})
