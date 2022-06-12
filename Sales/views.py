from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def salesPage(request):
    return HttpResponse('from salesPage')
def totalSales(request):
    return HttpResponse('from totalSales')
def salesfromouter(request):
    return HttpResponse('from salesfromouter')
def salesfrominner(request):
    return HttpResponse('from salesfrominner')                 