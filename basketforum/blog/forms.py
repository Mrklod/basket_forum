from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'registration-form__input'
    }))
    text = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'registration-form__input'
    }))
    photo = forms.CharField(widget=forms.FileInput(attrs={
        'class': 'registration-form__input'
    }))
    cat = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'registration-form__input'
    }))
    class Meta:
        model = Post
        fields = ('name','text','photo','cat')
