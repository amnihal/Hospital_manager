from django import forms
from .models import Departmentheads

class posthead(forms.ModelForm):
    class Meta:
        model = Departmentheads
        fields = '__all__'

        labels ={
            'dhead_name': "Name",
            'age' : "Age",
            'image' :"Profile image"  ,
            'description' :"Description",
            'department' :"Department",
        }
        