from django.shortcuts import render
from django.urls import reverse_lazy
from . import models
from django.views import generic
from .forms import OpinionForm
from .models import Opinion
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def destinations(request):
    all_destinations = models.Destination.objects.all()
    return render(request, 'destinations.html', { 'destinations': all_destinations})

class DestinationDetailView(generic.DetailView):
    template_name = 'destination_detail.html'
    model = models.Destination
    context_object_name = 'destination'

class CruiseDetailView(generic.DetailView):
    template_name = 'cruise_detail.html'
    model = models.Cruise
    context_object_name = 'cruise'

class InfoRequestCreate(SuccessMessageMixin, generic.CreateView):
    template_name = 'info_request_create.html'
    model = models.InfoRequest
    fields = ['name', 'email', 'cruise', 'notes']
    success_url = reverse_lazy('index')
    success_message = 'Thank you, %(name)s! We will email you when we have more information about %(cruise)s!'


class OpinionsView(generic.TemplateView):
    template_name = 'opinions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Puedes agregar lógica para obtener y pasar las opiniones aquí
        context['opinions'] = Opinion.objects.all()  # Obtener todas las opiniones
        context['form'] = OpinionForm()  # Agregar un formulario en el contexto
        return context

    def post(self, request, *args, **kwargs):
        form = OpinionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('opinions')  # Redirigir a la página de opiniones después de enviar el formulario
        else:
            # Si el formulario no es válido, puedes manejarlo según tus necesidades
            # Por ejemplo, podrías mostrar un mensaje de error en la misma página
            return render(request, self.template_name, {'form': form, 'opinions': Opinion.objects.all()})
