from django import forms

from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [ 'car_name', 'car_model', 'content', 'image' ]


class ContactForm(forms.Form):
	fullname = forms.CharField(max_length=64, required=True)
	email	 = forms.EmailField(required=True)
	content	 = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))

