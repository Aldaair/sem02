import math
from django.shortcuts import render

# Create your views here.

def index(request):
    context={
        'titulo':"CÁLCULO DEL VOLUMEN DE UN CILINDRO",
    }
    return render(request,'cilindro/formulario.html',context)
def enviar(request):
    diametro=float(request.POST['diametro'])
    altura=float(request.POST['altura'])
    volumen = math.pi * pow((diametro/2),2) * altura
    context = { 'volumen': volumen}  
    return render(request,'cilindro/respuesta.html',context)