from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from django import forms
from .models import ContactMessage, Profile


class RegisterForm(UserCreationForm):
  class Meta:
      model = get_user_model()
      fields = ('email', 'username', 'password1', 'password2')
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.helper = FormHelper()
      self.helper.form_show_labels = False


class LoginForm(AuthenticationForm):
  username = forms.CharField(label='Email / Username')
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.helper = FormHelper()
      self.helper.form_show_labels = False


class ProfileForm(forms.Form):
  email = forms.CharField(label='Почта:', max_length=80)
  first_name = forms.CharField(label='Имя:', max_length=80, required=True)
  last_name = forms.CharField(label='Фамилия:', max_length=80, required=True)

  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.helper = FormHelper()
      self.fields['email'].widget.attrs['readonly'] = ''

class ContactForm(forms.ModelForm):
  class Meta:
    model = ContactMessage
    fields = ('name', 'contact', 'contact_name', 'message')
    
  
  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.fields['message'].widget.attrs = {'rows': 3}
        self.fields['contact_name'].label = "Ваш никнейм/почта"