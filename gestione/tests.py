from django.test import TestCase
from django.http import Http404
from django.test.client import RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from array_persona import *
from .models import Persona
import generate_html
import views

# Classe che permette di testare l'integrita dei dati presenti nel model
class TestModel(TestCase):
    def test_martedi_notte(self):
        for i in range(0, len(persone)):
            self.assertLessEqual(int(persone[i].martedi_notte), 2)
    def test_anno_freq(self):
        for i in range(0, len(persone)):
            self.assertLessEqual(int(persone[i].martedi_notte), 5)
            self.assertGreaterEqual(int(persone[i].anno_freq), 1)

# Classe che permette di testare l'httpResponse di alcune views
class TestView(TestCase):
    # Creazione dell'utente anonimo
    def setUp(self):
        self.factory = RequestFactory()
        Persona.objects.all().delete()
        self.user = AnonymousUser()

    # in questo modo possiamo verificare che la pagina stampa non puo essere
    # raggiunta da un utente non loggato
    def test_stampa(self):
        request = self.factory.get('/stampa')
        request.user = self.user
        response = views.stampa(request)
        self.assertEqual(response.status_code, 302)