from django import forms

class BearbeitenForm(forms.Form):
    # die Eingabefelder mit beschreibendem Labeln
    vorname = forms.CharField(label="Vorname")
    nachname = forms.CharField(label="Nachname")
    strasse = forms.CharField(label="Strasse")
    plz = forms.CharField(label="Postleitzahl")
    ort = forms.CharField(label="Ort")
    # eine Eingabe für das Telefon ist nicht erforderlich
    telefon = forms.CharField(label="Telefon", required=False)