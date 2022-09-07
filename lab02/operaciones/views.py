from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context={
        'titulo':"Formulario",
    }
    return render(request,'operaciones/formulario.html',context)

def enviar(request):
    operacion=0
    #currentOpe = str(request.POST.getlist('operacion')).lower
    currentOpe = request.POST['operacion']
    num1= int(request.POST['num1'])
    num2= int(request.POST['num2'])
    if(currentOpe=="suma"):
        operacion=num1+num2
        context={'operacion': operacion}
    if(currentOpe=="resta"):
        operacion=num1-num2
        context={'operacion': operacion}
    if(currentOpe=="multi"):
        operacion=num1*num2
        context={'operacion': operacion}
    return render(request,'operaciones/respuesta.html',context)

