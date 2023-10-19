from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=70)
    email = forms.EmailField(max_length=100)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(max_length=3000, widget=forms.Textarea)