from django.forms import ModelForm
from .models import User, Commentaire, Restau, Reponse, image

from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'Nom': forms.TextInput(attrs={'class': 'form-control',
                                          'placeholder': 'Votre nom', 'name': 'nam'}),
            'mail': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre Email', 'name': 'mail'}),
            'sexe': forms.Select(attrs={'class': 'form-control'}),
            'MotPasse': forms.PasswordInput(
                attrs={'class': 'form-control', 'name': 'password', 'id': 'password', 'onkeyup': 'check();'}),
            'image': forms.FileInput(
                attrs={'type': 'file', 'id': 'customFile', 'name': 'filename', 'class': ' custom-file-input'}),
        }


class RepForm(forms.ModelForm):
    class Meta:
        model = Reponse
        fields = ['Contenu']
        widgets = {
            'Contenu': forms.Textarea(
                attrs={'class': 'textarea', 'placeholder': 'Votre Commentaire', 'rows': 1, 'cols': 35}),
        }


class CommentaireForm(forms.Form):
    Contenu = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control','placeholder': 'Entrez votre avis ici...', 'rows': 2, 'cols': 64}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'type': 'file', 'name': 'img_logo', 'class': 'dropzone'}),
                             required=False)


class NewArticleForm(forms.Form):
    c = [("1", "Option 1"), ("2", "Option 2")]
    choices = forms.ChoiceField(choices=c, label="Choices")


class indexChoice(forms.Form):
    villes = [
        ('restaurants à proximité de vous', 'restaurants à proximité de vous'),
        ('Rabat', 'Rabat'),
        ('Paris', 'Paris'),
        ('Tokyo', 'Tokyo'),
        ('Rome', 'Rome'),
        ('Mexico', 'Mexico'),
        ('Athènes', 'Athènes'),
    ]
    choix_adresse = forms.CharField(required=False, label='', widget=forms.Select(choices=villes,
                                                                                  attrs={'class': 'form-control'}))


class indexForm(forms.Form):
    autre_adresse = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Autre Adresse', 'size': 120, 'maxlength': 200}))
