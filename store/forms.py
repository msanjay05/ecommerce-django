from django.contrib.auth.models import User
from .models import Customer
from django import forms
from django.contrib.auth import authenticate
from django.forms.models import modelformset_factory


class RegistrationForm(forms.Form):
        user = forms.CharField(max_length=30, label='User Name')
        first_name=forms.CharField(max_length=50,label='First Name')
        last_name=forms.CharField(max_length=50,label='Last Name')
        email = forms.EmailField()
        password = forms.CharField(max_length=30, label='Password', widget=forms.PasswordInput(render_value=False))
        password_again = forms.CharField(max_length=30, label=' Check Password', widget=forms.PasswordInput(render_value=False))

        def clean(self):
        	if 'password' in self.cleaned_data and 'password_again' in self.cleaned_data:
        		if self.cleaned_data['password']!=self.cleaned_data['password_again']:
        			raise forms.ValidationError('both password match')
        	return self.cleaned_data

        def clean_user(self):
        	try:
        		User.objects.get(username=self.cleaned_data['user'])
        	except User.DoesNotExist:
        		return self.cleaned_data['user']
        	raise forms.ValidationError('user already  exists')


        def save(self):
        	username=self.cleaned_data['user']
        	email=self.cleaned_data['email']
        	password=self.cleaned_data['password']
        	new_user=User.objects.create_user(username=username,email=email,password=password,first_name=self.cleaned_data['first_name'],last_name=self.cleaned_data['last_name'])

        	new_customer=Customer.objects.create(user=new_user,email=email)



class LoginForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=User
		fields=['username','password']