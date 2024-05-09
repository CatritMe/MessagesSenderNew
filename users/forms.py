from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from mailing.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """Форма для регистрации пльзователя"""
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    """Форма редактирования профиля пользователя"""

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',)

    def __init__(self, *args, **kwargs):
        """скрытие пароля при редактировании"""
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class UserManagerForm(UserChangeForm):
    """Форма редактирования пользователя модератором"""

    class Meta:
        model = User
        fields = ('is_active',)
