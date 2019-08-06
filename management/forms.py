from django import forms
from .models import Class


class ClassCreateForm(forms.ModelForm):
    student_id = forms.CharField(max_length=150)
    parent_id = forms.CharField(max_length=150)

    class Meta:
        model = Class
        exclude = (
            'class_teacher',
            'students',
            'memo',
        )
        fields = '__all__'

    def __init__(self, class_teacher, *args, **kwargs):
        self.class_teacher = class_teacher
        super(ClassCreateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.class_teacher = self.class_teacher
        return super(ClassCreateForm, self).save(commit=commit)
