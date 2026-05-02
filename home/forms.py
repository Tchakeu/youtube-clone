from django import forms
from django.forms import TextInput

from .models import Comment


class CommentForm(forms.ModelForm):
    body = forms.CharField(max_length=2000, widget=TextInput(attrs={'placeholder': "Ajouter un commentaire"}))

    class Meta:
        model = Comment
        fields = ['body']
