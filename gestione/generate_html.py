import calendar
import array_persona
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
mese = str(month)+'/'+str(year)

table = """<table class="tg">
  <tr>
    <th class="tg-031e">"""+mese+"""</th>
    <th class="tg-031e">Giorno ACC</th>
    <th class="tg-031e">Notte ACC</th>
    <th class="tg-031e">Giorno NEO</th>
    <th class="tg-031e">Notte NEO</th>
    <th class="tg-031e">Giorno REPARTO</th>
    <th class="tg-031e">Notte REPARTO</th>
  </tr>
  <tr>
"""
counter = 1
for days in tupla4:
    table = table +'<td class="tg-031e">'+str(counter)+" "+str(days)+'</td>'
    for i in array_persona.nome:
            table = table+'<td class="tg-vn4c">'+i+'</td>'
    table = table + "</tr>"
    counter +=1
