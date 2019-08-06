from django import forms
from .models import Post


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)
        fields = '__all__'

    def __init__(self, author, *args, **kwargs):
        self.author = author
        super(UploadFileForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.author = self.author
        return super(UploadFileForm, self).save(commit=commit)


class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')
