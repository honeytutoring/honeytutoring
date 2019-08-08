from django import forms
from .models import Class, Schedule


class   ClassCreateForm(forms.ModelForm):
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


class ScheduleCreateForm(forms.ModelForm):
    class Meta:
        model = Schedule
        exclude = ('klass',)
        fields = '__all__'

    def __init__(self, klass_id, *args, **kwargs):
        self.klass_id = klass_id
        super(ScheduleCreateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.klass_id = self.klass_id
        return super(ScheduleCreateForm, self).save(commit=commit)
