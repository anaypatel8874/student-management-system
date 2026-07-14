from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student


# User Registration Form
class RegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User

        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]


# Student Form
class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = "__all__"

        widgets = {

            "name": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "roll_no": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "branch": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "semester": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "photo": forms.FileInput(attrs={
                "class": "form-control"
            }),
        }