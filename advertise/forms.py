from django import forms
from .models import Post


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Post
        # exclude = ('user',)
        fields = '__all__'


class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')
