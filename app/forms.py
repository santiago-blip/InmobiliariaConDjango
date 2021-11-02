from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.forms import fields
from django.forms.widgets import Widget
from .models import Usuario, Casa,GaleriaCasa
from django.forms import ModelForm


class UserRegisterForm(ModelForm):
     nombre = forms.CharField(max_length=50, widget=forms.TextInput(
         attrs={'class': 'inputFormRegistro', 'required': False}))
     apellido = forms.CharField(max_length=50, widget=forms.TextInput(
         attrs={'class': 'inputFormRegistro', 'required': False}))
     numeroCelular = forms.CharField(max_length=50, widget=forms.TextInput(
         attrs={'class': 'inputFormRegistro', 'required': False}))
     email = forms.EmailField(max_length=100, widget=forms.TextInput(
         attrs={'class': 'inputFormRegistro', 'required': False}))
     password = forms.CharField(max_length=100, widget=forms.PasswordInput(
         attrs={'class': 'inputFormRegistro', 'id': 'passR', 'required': False}))

     class Meta:
         model = Usuario
         fields = ['nombre', 'apellido', 'numeroCelular',
             'email', 'password', 'imagen']

     def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            return user

         
class LoginUser(forms.Form):
    email  = forms.EmailField(widget=forms.TextInput(attrs={'class':'divSessioninput','id':'Usuario'}))
    password  = forms.CharField(widget=forms.PasswordInput(attrs={'class':'divSessioninput','id':'Contrasena'}))


class CasaForm(forms.ModelForm):
    titulo  = forms.CharField(widget=forms.TextInput(attrs={'class':'inputFormRegistroCasa'}))
    descripcion  = forms.CharField(widget=forms.Textarea(attrs={'class':'areaFormRegistroCasa'}))
    imagen = forms.ImageField()
    class Meta:
         model = Casa
         fields = ['titulo','descripcion','imagen']

class GaleriaForm(forms.ModelForm):
    imagenGaleria = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'multiple':True
    }))
    class Meta:
        model = GaleriaCasa
        fields = ['imagenGaleria']
        
class CambioGaleriaImg(forms.ModelForm):
    class Meta:
        model = GaleriaCasa
        fields = ['imagenGaleria']

class CambioImgCasa(forms.ModelForm):
    class Meta:
        model = Casa
        fields = ['imagen']

class UpdateDatosPersona(forms.Form):
     nombre = forms.CharField(max_length=50, widget=forms.TextInput(
         attrs={'class': 'inputFormEditDatos', 'id':'InputNombre','required': False}))
     apellido = forms.CharField(max_length=50, widget=forms.TextInput(
         attrs={'class': 'inputFormEditDatos','id':'InputApellido' ,'required': False}))
     numeroCelular = forms.CharField(max_length=50, widget=forms.TextInput(
         attrs={'class': 'inputFormEditDatos', 'id':'InputNumero' ,'required': False}))
     titulo = forms.CharField(max_length=100, widget=forms.TextInput(
         attrs={'class': 'inputFormEditDatos', 'id':'InputTitulo' ,'required': False}))
     descripcion = forms.CharField(max_length=100, widget=forms.Textarea(
         attrs={'class': 'textareaT', 'id':'InputDesc' ,'required': False}))
