from django import forms
from django.forms import ModelForm

from .models import Product


class Add_Product_Form(ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ('available',)

    template_name = 'form/input_form.html'
