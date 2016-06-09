from django import forms
from django.forms import ModelForm, Textarea, TextInput
from .models import AnaliseDesgaste
    
class AnaliseDesgasteForm(forms.ModelForm):
	class Meta:
		model = AnaliseDesgaste
		fields = ('tempo_inicio', 'tempo_fim', 'peso')        