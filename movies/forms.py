from django import forms
from .models import Movie, Genre, Comment

class CommentForm(forms.ModelForm):
    score = forms.IntegerField(label="")
    content = forms.CharField(label="")
    class Meta:
        model = Comment
        fields = ['score', 'content',]