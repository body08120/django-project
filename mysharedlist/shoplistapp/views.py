from django.shortcuts import render
from django.template import loader
from .models import Store
from django.http import HttpResponse, JsonResponse

# Create your views here.

# Renvoyer la table Store en html
def index(request):
    stores = Store.objects.all()
    template = loader.get_template('index.html')
    context = {'stores': stores}
    return HttpResponse(template.render(context, request))

# Renvoyer la table Store en json
def index_json(request):
    stores = Store.objects.all().values()
    return JsonResponse(data=list(stores), safe=False)