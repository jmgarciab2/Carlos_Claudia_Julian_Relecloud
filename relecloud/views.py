from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . import models
from django.views import generic
from .forms import OpinionForm
from .models import Opinion
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

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
    success_message = 'Email confirmation successful'

    def form_valid(self, form):
        response = super().form_valid(form)
        subject = 'Confirmation of InfoRequest'
        message = render_to_string('confirmation_email.html', {'name': form.cleaned_data['name'], 'cruise': form.cleaned_data['cruise']})
        plain_message = strip_tags(message)
        from_email = 'is2practicacorreo@gmail.com'
        to_email = form.cleaned_data['email']
        send_mail(subject, plain_message, from_email, [to_email], html_message=message)
        return response


class OpinionsView(generic.TemplateView):
    template_name = 'opinions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Se puede agregar lógica para obtener y pasar las opiniones aquí
        context['opinions'] = Opinion.objects.all()  # Obtiene todas las opiniones
        context['form'] = OpinionForm()  # Agrega un formulario en el contexto
        return context

    def post(self, request, *args, **kwargs):
        form = OpinionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('opinions')  # Redirige a la página de opiniones después de enviar el formulario
        else:
            # Si el formulario no es válido, podemos manejarlo según queramos
            # Por defecto, muestra un mensaje de error en la misma página
            return render(request, self.template_name, {'form': form, 'opinions': Opinion.objects.all()})
