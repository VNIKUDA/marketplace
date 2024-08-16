from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistrationForm(UserCreationForm):
    usable_password = None
