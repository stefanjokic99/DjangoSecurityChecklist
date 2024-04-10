from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField


class CreateUserForm(UserCreationForm):
  captcha = ReCaptchaField()
  
  class Meta:
    model = User
    fields = ["username", "email", "password1", "password2"]

  