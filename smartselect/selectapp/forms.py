from django import forms

class rangeform(forms.Form):
    price_range_=forms.ChoiceField(choices=[['500000-1500000','5000-15000'],['1000000-2000000','10000-20000']])