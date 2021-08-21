from django import forms
from .models import Books
from barrow.models import Barrow

class PostForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = [
            'id',
            'title',
            'author',


        ]

