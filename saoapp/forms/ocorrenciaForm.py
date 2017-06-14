# coding: utf-8

from django import forms
from saoapp.models import OcorrenciaModel


class OcorrenciaForm(forms.ModelForm):
    class Meta:
        model = OcorrenciaModel
        fields = "__all__"