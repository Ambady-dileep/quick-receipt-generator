from django import forms 
from .models import Receipt,Item
from django.forms import inlineformset_factory 

class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields =['customer']

ItemFormSet = inlineformset_factory(
    Receipt, Item, fields = ['name','quantity','unit','price'],extra=1
)
