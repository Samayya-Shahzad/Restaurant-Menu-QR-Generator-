from django import forms

class QRcodeform(forms.Form):
    restaurant_name = forms.CharField(max_length=50, 
                                      label='Restuarant Name',
                                      widget= forms.TextInput(attrs={
                                          'class':'form-control',
                                          'placeholder':'Enter Restaurant name'
                                      }
                                      )
                                      )
    url = forms.URLField(max_length=200, 
                         label='Paste menu URL',
                         widget= forms.URLInput(attrs={
                                          'class':'form-control',
                                          'placeholder':'Enter Menu URL'
                                      }
                                      )
                         )
