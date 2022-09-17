from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'comment', 
            
            )
        widgets ={
            'comment' : forms.TextInput(attrs={
                'class' : 'form-control'
            }), 

        }