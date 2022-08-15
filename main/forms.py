from django import forms
from .models import Homework

class AddHomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ["lesson", "content", "photo", "deadline"]
        widgets = {
            'lesson': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),

        }