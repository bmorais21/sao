# coding: utf-8

from django import forms
from saoapp.models import ProfessorModel

class ProfessorForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'required': 'True', 'pattern': '^[a-zA-Z-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ\s]*$', 'title': 'Apenas letras.', 'maxlength': 45, 'placeholder': 'Nome'}
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'required': 'True', 'pattern': '^[a-zA-Z-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ\s]*$', 'title': 'Apenas letras.', 'maxlength': 45, 'placeholder': 'Sobrenome'}
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'required': 'True', 'maxlength': 45, 'placeholder': 'E-Mail'}
        )
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'required': 'True', 'maxlength': 45, 'placeholder': 'Nome'}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'required': 'True', 'maxlength': 45, 'placeholder': 'Senha'}
        )
    )

    class Meta:
        model = ProfessorModel
        exclude = ('date_joined', 'is_staff', 'user_permissions', 'groups', 'last_login', 'is_superuser',
                   'is_active')

    def save(self, commit=True):
        professor = super(ProfessorForm, self).save(commit=False)
        professor.set_password(self.cleaned_data['password'])
        if commit:
            professor.save()
        return professor