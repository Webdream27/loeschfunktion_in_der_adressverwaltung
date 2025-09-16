"""######
views.py
######"""

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

# die Klasse mit dem Modell
from .models import Adresse

# die generische View für die Liste
class AdresseListView(ListView):
    model = Adresse
    template_name = "adressverwaltung/liste.html"
    context_object_name = "adressen"

# die generische View für die Details
class AdresseDetailView(DetailView):
    model = Adresse
    template_name = "adressverwaltung/detail.html"
    context_object_name = "adresse"
    
# die generische View für das Erstellen
class AdresseCreateView(CreateView):
    model = Adresse
    fields = "__all__"
    template_name = "adressverwaltung/bearbeiten.html"
    success_url = "/"
    
    def get_context_data(self):
        context = super().get_context_data()
        context["ueberschrift"] = "Neuer Eintrag"
        return context
    
# die generische View für das Bearbeiten
class AdresseUpdateView(UpdateView):
    model = Adresse
    fields = "__all__"
    template_name = "adressverwaltung/bearbeiten.html"
    success_url = "/"
    
    def get_context_data(self):
        context = super().get_context_data()
        context["ueberschrift"] = "Daten bearbeiten"
        return context
