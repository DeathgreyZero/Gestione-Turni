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
        mese = request.POST.get('mese')
        anno = request.POST.get('anno')
        generate_html.change_data(mese,anno)
        generate_html.reset()
        generate_html.gen_turno()
        HTML = generate_html.table
        return render(request,"gestione/stampa.html",{"HTML":HTML})
    if(request.POST.get('salva_xls')):
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=turni.xls'
        generate_html.save_xls(response)
        return response
    if(request.POST.get('load_mat')):
        generate_html.load_mat()
    return render(request,"gestione/stampa.html")

@login_required
def orario_personale(request):
    generate_html.load_mat(request.user)
    Tab = generate_html.table_personale
    return render(request,'gestione/orario_personale.html',{"Tab":Tab})

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')