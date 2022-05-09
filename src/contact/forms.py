from django import forms

from .models import Response


class ContactForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ('name', 'email', 'message')
        labels = {
            'name': 'Your name',
            'email': 'Your email',
            'message': 'How can I help?',
        }
