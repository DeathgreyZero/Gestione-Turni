from django.conf.urls import include,url
from . import views

urlpatterns = ('',
    url(r'^$', 'gestione.views.index'),
    url(r'^stampa/$','gestione.views.stampa'),
    url(r'^orario_personale/$','gestione.views.orario_personale'),
    url(r'^logout/$','gestione.views.logout'),
)
