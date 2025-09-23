from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from .forms import ContactForm
from .forms import LoginForm

from django.views.generic import CreateView
from .models import Person
from django.contrib.auth import login, authenticate 

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .utils import reporteSeleccionado
from .utils import leeMysql

from rest_framework import viewsets
from .serializer import consulta1Serializer
from .serializer import DetalleVulnerabilidadSerializer
from .serializer import GraficaVulnerabilidadesSerializer
from .models import consulta1
from .models import DetalleVulnerabilidad
from .models import GraficaVulnerabilidades


#ejemplos basicos
def inicio(request):
    return HttpResponse("Esto se llama cuando se visita gastos/")

def hola(request):
    return HttpResponse("Ahora pediste gastos/hola")

def agregar_gasto(request):
    html = """
    <h1>Agregar gasto</h1>
    <p>Podemos mostrar HTML, pero es más interesante cuando usamos
    <strong>plantillas</strong> y motores ;)</p>
    """
    return HttpResponse(html)


# formulario
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data here (e.g., send email)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            elegir = form.cleaned_data['elegir']
            # For demo, just print to console
            print(f"Received message from {name} ({email}): {message}")
            return render(request, 'aplicacionweb1/thank_you.html', {'name': name})
    else:
        form = ContactForm()
    return render(request, 'aplicacionweb1/contact.html', {'form': form})
    #return render(request, 'aplicacionweb1/person_form.html', {'form': form})


class PersonCreateView(CreateView):
    model = Person
    fields = ('name', 'email', 'job_title', 'bio')



def sign_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Process form data here (e.g., send email)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            return render(request, 'aplicacionweb1/reporteria-resultado.html', {'username': username})
    else:
        form = LoginForm()
    return render(request, 'aplicacionweb1/login.html', {'form': form}) 

def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
            else:
                message = 'Login failed!'
    return render(
        #request, 'authentication/login.html', context={'form': form, 'message': message})
        request, 'aplicacionweb1/login.html', context={'form': form, 'message': message})


@csrf_exempt
def json_handler(request):
    if request.method == 'POST':
        try:
            #valor=1
            valor=request.GET["reporte"]
            #compartimento=request.GET["compartimento"]
            print("valor =",valor," de tipo=",type(valor))
            #print("compartimento =",compartimento," de tipo=",type(compartimento))
            #print(request.GET["reporte"])
            #print(valor)
            #data = json.loads(request.body)
            #valor = request.reporte
            #valor = request['reporte']
            #form = forms.LoginForm(request.POST)
            #valor=form.cleaned_data['reporte']
            #response = {
            #    'status': 'success',
            #    'data': reporteSeleccionado(1)
            #}
            

            response = reporteSeleccionado(int(valor))
            #response = leeMysql()
        except json.JSONDecodeError:
            response = {
                'status': 'error',
                'message': 'Invalid JSON data'
            }
    else:
        response = {
            'status': 'error',
            'message': 'Only POST requests are allowed'
        }
    #return JsonResponse(response)    
    return response    

def my_view(request):
    if request.method == 'GET':
        #data = {'name': 'Alice', 'email': 'alice@example.com'} # create a dictionary
        #data = reporteSeleccionado(2)
        data = leeMysql()
        return JsonResponse(data, status=200, safe=True) # return the dictionary as a JSON response



class consulta1ViewSet(viewsets.ModelViewSet):
    queryset = consulta1.objects.all()
    serializer_class = consulta1Serializer


class DetalleVulnerabilidadViewSet(viewsets.ModelViewSet):
    queryset = DetalleVulnerabilidad.objects.all()
    serializer_class = DetalleVulnerabilidadSerializer

class GraficaVulnerabilidadesViewSet(viewsets.ModelViewSet):
    queryset = GraficaVulnerabilidades.objects.all()
    serializer_class = GraficaVulnerabilidadesSerializer

