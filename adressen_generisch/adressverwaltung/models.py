"""######
models.py
######"""

from django.db import models

# die Klasse für das Modell
class Adresse(models.Model):
    vorname = models.CharField(max_length=50)
    nachname = models.CharField(max_length=50)
    strasse = models.CharField(max_length=50)
    plz = models.CharField(max_length=5)
    ort = models.CharField(max_length=50)
    telefon = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.vorname + " " + self.nachname