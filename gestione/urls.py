from django.conf.urls import include,url
from . import views

urlpatterns = ('',
    url(r'^$', 'gestione.views.index'),
    url(r'^stampa/','gestione.views.stampa')
)
