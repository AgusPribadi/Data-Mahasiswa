from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Record

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# - Register/Create a User
class CreateUserForm(UserCreationForm):
    class Meta:
        
        model = User
        fields = ['username', 'password1', 'password2']

# - Login a User
class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# - Create a Record
class CreateRecordForm(forms.ModelForm):
    class Meta:

        model = Record
        fields = ['nama_awal', 'nama_akhir', 'nim', 'semester', 'kelas', 'email', 'nomor_hp', 'alamat', 'kota', 'provinsi']

# - Update a Record
class UpdateRecordForm(forms.ModelForm):
    class Meta:

        model = Record
        fields = ['nama_awal', 'nama_akhir', 'nim', 'semester', 'kelas', 'email', 'nomor_hp', 'alamat', 'kota', 'provinsi']
    