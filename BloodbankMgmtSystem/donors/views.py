from django.http import HttpResponse
from django.template import loader
from .models import Donors

def index(request):
  template = loader.get_template('donors.html')
  return HttpResponse(template.render())

def donors(request):
  mydonors = Donors.objects.all().values()
  template = loader.get_template('donorslist.html')
  context = {
    'mydonors': mydonors,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mydonors = Donors.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mydonors': mydonors,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())