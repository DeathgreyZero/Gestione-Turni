from django.shortcuts import render,render_to_response
import generate_html
import array_persona

def index(request):
    print 'Index'
    return render(request,'gestione/index.html')


def stampa(request):
    HTML = generate_html.table
   # print array_persona.nome

    return render(request,"gestione/stampa.html",{"HTML":HTML})
