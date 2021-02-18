from django import forms
from django.contrib.auth.models import User


class ProfileForm(forms.Form):

    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)

    picture = forms.ImageField()


class SignupForm(forms.Form):

    """Sign up form."""
    username = forms.CharField(
        min_length=4,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control',
                'required': True
            }
        )
    )
    password = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control',
                'required': True
            }
        )
    )
    password_confirmation = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password Confirmation',
                'class': 'form-control',
                'required': True
            }
        )
    )

    first_name = forms.CharField(
        min_length=3,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First name',
                'class': 'form-control',
                'required': True
            }
        )
    )
    last_name = forms.CharField(
        min_length=3,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last name',
                'class': 'form-control',
                'required': True
            }
        )
    )

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "email",
                "class": "form-control",
                'required': True
            }
        )
    )

    def clean_username(self):
        """ Username must be unique """

        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()

        if username_taken:
            raise forms.ValidationError('Username is already in use')
        return username

    
    def clean(self):
        """ Verify password confirmation match """
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Password confirmation is incorrect')
        return password
