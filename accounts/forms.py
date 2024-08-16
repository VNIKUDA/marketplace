from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class RegistrationForm(UserCreationForm):
    usable_password = None

    class Meta:
        model = get_user_model()
        fields = ["email", "first_name", "last_name", "password1", "password2"]