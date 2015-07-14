from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.decorators import user_passes_test
from django.contrib import auth
from django.http import HttpResponse
import generate_html
import calendar

mese_anno = 0
mese = 0

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
    festivi = []
    lista_notti_effettuate = []
    global mat
    global mese_anno
    global mese
    if(request.POST.get('gen_turni')):
        mese = request.POST.get('mese')
        anno = request.POST.get('anno')

        if mese == 1:
            festivi = [1, 6]
        if mese == 2:
            festivi = [17]
        if mese == 4:
            festivi = [25]
        if mese == 5:
            festivi = [1]
        if mese == 6:
            festivi = [2]
        if mese == 8:
            festivi = [15]
        if mese == 11:
            festivi = [1]
        if mese == 12:
            festivi = [8, 25, 26]

        ret = generate_html.crea_liste(int(mese), int(anno))

        tupla4    = ret[0]
        mat       = ret[1]
        mese_anno = ret[2]

        table = """<table class="tg">
          <tr>
            <th class="tg-031e">""" + mese_anno + """</th>
            <th class="tg-031e">Giorno ACC</th>
            <th class="tg-031e">Notte ACC</th>
            <th class="tg-031e">Giorno NEO</th>
            <th class="tg-031e">Notte NEO</th>
            <th class="tg-031e">Giorno REPARTO</th>
            <th class="tg-031e">Notte REPARTO</th>
          </tr>
          <tr>
        """

        generate_html.reset()
        HTML = generate_html.gen_turno(table, tupla4, mat, lista_notti_effettuate, festivi, mese)

        return render(request,"gestione/stampa.html",{"HTML":HTML})
    if(request.POST.get('salva_xls')):
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=turni.xls'
        generate_html.save_xls(response, mese_anno, mat)
        return response
    if(request.POST.get('load_mat')):
        table_personale = """<table class="tg">
          <tr>
            <th class="tg-031e">""" + mese_anno + """</th>
            <th class="tg-031e">Giorno ACC</th>
            <th class="tg-031e">Notte ACC</th>
            <th class="tg-031e">Giorno NEO</th>
            <th class="tg-031e">Notte NEO</th>
            <th class="tg-031e">Giorno REPARTO</th>
            <th class="tg-031e">Notte REPARTO</th>
          </tr>
          <tr>
        """

        generate_html.load_mat(user=request.user, table_personale=table_personale, mese=mese)

    return render(request, "gestione/stampa.html")

@login_required
def orario_personale(request):
    global mese
    global mese_anno
    table_personale = """<table class="tg">
        <tr>
        <th class="tg-031e">""" + str(mese_anno) + """</th>
        <th class="tg-031e">Giorno ACC</th>
        <th class="tg-031e">Notte ACC</th>
        <th class="tg-031e">Giorno NEO</th>
        <th class="tg-031e">Notte NEO</th>
        <th class="tg-031e">Giorno REPARTO</th>
        <th class="tg-031e">Notte REPARTO</th>
        </tr>
        <tr>
    """
    Tab = generate_html.load_mat(user=request.user, table_personale=table_personale, mese=mese)
    return render(request,'gestione/orario_personale.html',{"Tab":Tab})

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')