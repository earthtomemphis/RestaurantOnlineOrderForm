from django.forms import ModelForm
from django import forms
from . models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'delivery_pickup': forms.Select(attrs={'class': 'form-control'}),
            'address_line1': forms.TextInput(attrs={'class': 'form-control'}),
            'address_line2': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
            'menu_item1': forms.TextInput(attrs={'class': 'form-control'}),
            'menu_item2': forms.TextInput(attrs={'class': 'form-control'}),
            'menu_item3': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_method': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),
            'password2': forms.TextInput(attrs={'class': 'form-control'}),
        }