from django import forms
from .models import User,Elite,Pre,Nor,Bus

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields='__all__'
        widgets = {
            'password': forms.PasswordInput(),
            'pid':forms.HiddenInput(),
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')
        widgets = {
            'password': forms.PasswordInput(),
        }

class EliteForm(forms.ModelForm):
    class Meta:
        model=Elite
        fields='__all__'
        # cat=Elite.objects.get('category')
        # if cat == ('AC sleeper' or 'Non-AC sleeper'):
        #     pass
        # else:
        #     # fields='__all__'
        #     exclude=['upper_births','lower_births']
        widgets={
            'depature':forms.DateTimeInput(format=('%m/%d/%Y%H%M%S'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
            



class PreForm(forms.ModelForm):
    class Meta:
        model=Pre
        fields='__all__'
        widgets={
            'depature':forms.DateTimeInput(format=('%m/%d/%Y%H%M%S'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
         
        }

class NorForm(forms.ModelForm):
    class Meta:
        model=Nor
        fields='__all__'
        widgets={
            'depature':forms.DateTimeInput(format=('%m/%d/%Y%H%M%S'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            
        }