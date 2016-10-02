from django import forms
class Form(forms.Form):
	name=forms.CharField(label='Your Name',widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Full Name'}))
	phone_number=forms.CharField(label='Phone NUmber',widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valid Phone Number'}))
	description=forms.CharField(label='Your Description',widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tell us about yourself'}))

class Books_Form(forms.Form):
	name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Book Name'}))
	author=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Author'}))
class Search_Form(forms.Form):
	text=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Search for your favourite books'}))
	