from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    print 'Index'
    return render(request,'gestione/index.html')



def stampa(request):
    print 'Sto Stampando'
    test = 'Mario'
    return render(request,"gestione/stampa.html",{"test":test})
