from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    print 'Index'
    if request.method == 'POST':
        user = request.POST['user']
        password = request.POST['password']
        login(user,password)

    return render(request,'gestione/index.html')



def login(user,password):
    print "Username "+user+"Pass: "+password
