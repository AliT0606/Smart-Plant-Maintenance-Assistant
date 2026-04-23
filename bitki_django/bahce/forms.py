from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Plant, Note, Task


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'species', 'plant_type', 'location', 'water_frequency', 'light_need', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Örn: Barış Çiçeğim', 'class': 'form-input'}),
            'species': forms.TextInput(attrs={'placeholder': 'Örn: Spathiphyllum', 'class': 'form-input'}),
            'plant_type': forms.Select(attrs={'class': 'form-input'}),
            'location': forms.TextInput(attrs={'placeholder': 'Örn: Salon, Balkon...', 'class': 'form-input'}),
            'water_frequency': forms.Select(attrs={'class': 'form-input'}),
            'light_need': forms.Select(attrs={'class': 'form-input'}),
            'image': forms.FileInput(attrs={'class': 'form-file', 'accept': 'image/*'}),
        }
        labels = {
            'name': 'Bitki Adı',
            'species': 'Bilimsel Ad (İsteğe Bağlı)',
            'plant_type': 'Tür',
            'location': 'Konum',
            'water_frequency': '💧 Sulama Sıklığı',
            'light_need': '☀️ Işık İhtiyacı',
            'image': 'Fotoğraf (İsteğe Bağlı)',
        }


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Çiçeğiniz hakkında notlar...',
                'rows': 4,
                'class': 'form-input'
            })
        }
        labels = {'content': ''}


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'email@ornek.com', 'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Kullanıcı adı', 'class': 'form-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'placeholder': 'Şifre', 'class': 'form-input'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Şifre tekrar', 'class': 'form-input'})


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Kullanıcı adı', 'class': 'form-input'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Şifre', 'class': 'form-input'})
