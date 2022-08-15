from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django.core.validators import EmailValidator
from django import forms

from game_sessions.models import Player
from .selectors import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
                            # widget=forms.TextInput(attrs={'type': 'email', 'placeholder': 'Enter email'}),
                            # validators=[EmailValidator('Invalid email')])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'login-form'
        self.helper.form_class = 'login-form'
        self.helper.add_input(Submit('login', 'Login', css_class='w-100'))

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #
    #     if not authenticate(email):
    #         raise forms.ValidationError('Email does not exists')
    #
    #     return email


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['email', 'first_name', 'last_name']

    def clean(self):
        email = self.cleaned_data.get('email')

        if Player.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Duplicate email')

        return self.cleaned_data

    def save(self, commit=True):
        instance = super(RegisterForm, self).save(commit=False)
        instance.set_password('randompassword')
        instance.username = f'{instance.first_name}.{instance.last_name}'.lower()

        if commit:
            instance.save()

        return instance
