from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello from Django')

def test(request):
    # Récupérer les données d'un utilisateur depuis la base de données.
    # Stocker ces données dans un model (crée pour)
    # Intégrer les attributs de l'objet dans le html

    html = ''
    return HttpResponse(html)