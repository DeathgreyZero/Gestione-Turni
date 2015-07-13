from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.decorators import user_passes_test
from django.contrib import auth
from django.http import HttpResponse
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
    if(request.POST.get('gen_turni')):
        generate_html.reset()
        generate_html.gen_turno()
        HTML = generate_html.table
        return render(request,"gestione/stampa.html",{"HTML":HTML})
    else:
        HTML = generate_html.table
    if(request.POST.get('salva_xls')):
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=turni.xls'
        generate_html.save_xls(response)
        return response
    return render(request,"gestione/stampa.html",{"HTML":HTML})

@login_required
def orario_personale(request):
    return render(request,'gestione/orario_personale.html')

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')