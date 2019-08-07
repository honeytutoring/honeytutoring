from django import forms
from .models import QandA

class QuestionForm(forms.ModelForm):
    class Meta:
        model = QandA
        fields = (
            'title',
            'content',
        )
class AnswerForm(forms.ModelForm):
    class Meta:
        model = QandA
        fields = (
            'answer',
        )