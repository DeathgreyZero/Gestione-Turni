from django.shortcuts import render,render_to_response
import generate_html
import array_persona

def index(request):
    print 'Index'
    return render(request,'gestione/index.html')


def stampa(request):
    tupla3 = generate_html.tupla3
    tupla4 = generate_html.tupla4
    HTML = generate_html.table
   # print array_persona.nome

    return render(request,"gestione/stampa.html",{"tupla3":tupla3,"tupla4":tupla4,"array_persona":array_persona.nome,"HTML":HTML})
