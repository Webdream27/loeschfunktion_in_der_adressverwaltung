from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

# die Klasse mit dem Modell
from .models import Adresse

# die Klasse mit den Formularen
from .forms.forms import BearbeitenForm

# die Funktion für die erste Seite
def home_page_view(request):
    # wir beschaffen uns alle Adressen
    adressen = Adresse.objects.all()
    template = loader.get_template("adressverwaltung/liste.html")
    context = {
        "adressen": adressen,
    }
    return HttpResponse(template.render(context, request))

# die Funktion zum Bearbeiten
def bearbeiten(request, kunden_id):
    # die Adresse beschaffen
    adresse = Adresse.objects.get(id=kunden_id)
    # wurde die Seite über POST aufgerufen?
    if request.method == "POST":
        # dann erzeugen wir ein Formular mit den Daten
        form = BearbeitenForm(request.POST)
        # sind alle Daten korrekt eingegeben worden?
        if form.is_valid():
            # dann beschaffen wir uns den Eintrag und speichern ihn
            adresse.vorname=form.cleaned_data["vorname"]
            adresse.nachname=form.cleaned_data["nachname"]
            adresse.strasse=form.cleaned_data["strasse"]
            adresse.plz=form.cleaned_data["plz"]
            adresse.ort=form.cleaned_data["ort"]
            adresse.telefon=form.cleaned_data["telefon"]          
            adresse.save()
            # und wir wechseln wieder zurück zur Startseite
            return HttpResponseRedirect("/")
    # wenn der Aufruf nicht über POST erfolgt ist
    else:
        # erzeugen wir ein Formular mit den Daten
        form = BearbeitenForm(initial={"vorname": adresse.vorname, "nachname": adresse.nachname, "strasse": adresse.strasse, "plz": adresse.plz, "ort": adresse.ort, "telefon": adresse.telefon})  

    # und das Formular aufrufen
    return HttpResponse(render(request, "adressverwaltung/bearbeiten.html", {"ueberschrift": "Daten bearbeiten", "form": form}))

# die Funktion zum Erstellen
def neu(request):
    # wurde die Seite über POST aufgerufen?
    if request.method == "POST":
        # dann erzeugen wir ein Formular mit den Daten
        form = BearbeitenForm(request.POST)
        # sind alle Daten korrekt eingegeben worden?
        if form.is_valid():
            # dann beschaffen wir uns die Daten, erzeugen einen neuen Eintrag und speichern ihn
            vorname=form.cleaned_data["vorname"]
            nachname=form.cleaned_data["nachname"]
            strasse=form.cleaned_data["strasse"]
            plz=form.cleaned_data["plz"]
            ort=form.cleaned_data["ort"]
            telefon=form.cleaned_data["telefon"]          
            adresse = Adresse(vorname=vorname, nachname=nachname, strasse=strasse, plz=plz, ort=ort, telefon=telefon)
            adresse.save()
            # und wir wechseln wieder zurück zur Startseite
            return HttpResponseRedirect("/")
    # wenn der Aufruf nicht über POST erfolgt ist
    else:
        # erzeugen wir ein leeres Formular
        form = BearbeitenForm()  

    # und das Formular aufrufen
    return HttpResponse(render(request, "adressverwaltung/bearbeiten.html", {"ueberschrift": "Neuer Eintrag", "form": form}))

# die Funktion zum Löschen 
def loeschen(request, kunden_id):
    adresse = get_object_or_404(Adresse, id=kunden_id)
    adresse.delete()
    return HttpResponseRedirect("/")