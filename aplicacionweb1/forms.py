from django import forms
from .models import Post
from crispy_forms.helper import FormHelper

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Full Name')
    #email = forms.EmailField(label='Email Address')
    message = forms.CharField(widget=forms.Textarea, label='Your Message')
    CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
    elegir = forms.ChoiceField(choices=CHOICES)
    like_website = forms.TypedChoiceField(
        label = "Do you like this website?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
