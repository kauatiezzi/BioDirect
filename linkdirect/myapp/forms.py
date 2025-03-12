# myapp/forms.py
from django import forms
from .models import UserProfile, Button

class UserProfileForm(forms.ModelForm):
    theme_color = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'color'}),
        required=False,  # Torna o campo opcional
        label='Cor de tema'
    )
    class Meta:
        model = UserProfile
        fields = ['photo', 'custom_url', 'nome_empresa', 'instagram', 'whatsapp', 'linkedin', 'theme_color']
        labels = {
            'photo': 'Foto',
            'custom_url': 'URL personalizado',
            'nome_empresa': 'Nome comercial',
            'instagram': 'Instagram',
            'whatsapp': 'WhatsApp',
            'linkedin': 'LinkedIn',
            'theme_color': 'Cor de tema',
        } 

class ButtonForm(forms.ModelForm):
    class Meta:
        model = Button
        fields = ['name', 'url']    
        labels = {
            'name': 'TITULO DO BOTÃO',
            'url': 'SEU URL PERSONALIZADO'
        }