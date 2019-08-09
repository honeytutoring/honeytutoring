from django import forms
from .models import Class, Schedule, Memo


class ClassCreateForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = (
            'class_name',
            'description',
            'subject',
            'etc',
        )

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


class MemoCreateForm(forms.ModelForm):
    class Meta:
        model = Memo
        exclude = ('klass',)
        fields="__all__"

    def __init__(self, klass_id, *args, **kwargs):
        self.klass_id = klass_id
        super(MemoCreateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.klass_id = self.klass_id
        return super(MemoCreateForm, self).save(commit=commit)
