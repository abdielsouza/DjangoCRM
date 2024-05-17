from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Endereço de email'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sobrenome'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Nome de usuário'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Precisa de 150 caracteres ou menos. Letras, dígitos e @/./+/-/_ apenas.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Sua senha não pode ser tão parecida com suas outras informações pessoais.</li><li>A senha precisa ter no  mínimo 8 caracteres.</li><li>Sua senha não pode ser algo muito comum.</li><li>Sua senha não pode ser toda numérica.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirme a senha'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Digite a mesma senha de antes.</small></span>'	




# Create Add Record Form
class AddRecordForm(forms.ModelForm):
	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nome", "class":"form-control"}), label="")
	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Sobrenome", "class":"form-control"}), label="")
	email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
	phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Telefone", "class":"form-control"}), label="")
	address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Endereço", "class":"form-control"}), label="")
	city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Cidade", "class":"form-control"}), label="")
	state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Estado", "class":"form-control"}), label="")
	zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Código Postal", "class":"form-control"}), label="")

	class Meta:
		model = Record
		exclude = ("user",)