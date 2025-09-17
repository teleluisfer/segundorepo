from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from .forms import ContactForm

from django.views.generic import CreateView
from .models import Person


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



from django.shortcuts import render
 
def indexGrafica(request):
    developer_work_week_data = [
        { "name": "Writing Code", "y": 30.7 },
        { "name": "Debugging", "y": 36.4 },
        { "name": "Problem Solving", "y": 3.7 },
        { "name": "Firefighting", "y": 20.1 },
        { "name": "Overhead", "y": 9.1 }
    ]
 
  return render(request, 'grafica.html', { "developer_work_week_data" : developer_work_week_data })    
