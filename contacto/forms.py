from django import forms
from django.forms import ModelForm
from contacto.models import Consulta
from django import forms
from captcha.fields import CaptchaField

# pip install django-simple-captcha


class ConsultaForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Consulta
        fields = [
            "nombre",
            "descripcion",
            "mail",
            "telefono",
        ]

    def send_email(self):
        # send email using the self.cleaned_data dictionary

        nombre = self.cleaned_data["nombre"]
        descripcion = self.cleaned_data["descripcion"]
        mail = self.cleaned_data["mail"]
        telefono = self.cleaned_data["telefono"]

        print("enviando datos")
        print(nombre, descripcion, mail, telefono)
