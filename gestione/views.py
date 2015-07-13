from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponseRedirect,render_to_response
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.decorators import user_passes_test
from django.contrib import auth
import generate_html


def index(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_superuser:
            print 'Ola Capo'
            login(request,user)
            return HttpResponseRedirect('/stampa')
        if user.is_active:
            login(request, user)
            print 'credenziali esatte'
            return HttpResponseRedirect('/orario_personale')
        else:
            print 'sei disabilitato'
    else:
        print 'errore nelle credenziali'
    return render(request,'gestione/index.html')

@user_passes_test(lambda u: u.is_superuser)
def stampa(request):
    generate_html.reset()
    HTML = generate_html.table
    return render(request,"gestione/stampa.html",{"HTML":HTML})

@login_required
def orario_personale(request):
    return render(request,'gestione/orario_personale.html')

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')