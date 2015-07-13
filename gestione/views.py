from django.shortcuts import render
import generate_html

def index(request):
    return render(request,'gestione/index.html')


def stampa(request):
    generate_html.reset()
    HTML = generate_html.table
    return render(request,"gestione/stampa.html",{"HTML":HTML})
