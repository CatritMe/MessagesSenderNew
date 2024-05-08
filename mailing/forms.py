from django import forms
from django.forms import BooleanField

from mailing.models import Client, Mail, Mailing


class StyleFormMixin(forms.ModelForm):
    """Класс стилизации форм"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ClientForm(StyleFormMixin, forms.ModelForm):
    """Форма для редактирования получателя"""

    class Meta:
        model = Client
        exclude = ('user',)


class MailForm(StyleFormMixin, forms.ModelForm):
    """Форма для редактирования сообщения"""

    class Meta:
        model = Mail
        exclude = ('user',)


class MailingForm(StyleFormMixin, forms.ModelForm):
    """Форма для редактирования сообщения"""

    class Meta:
        model = Mailing
        exclude = ('status', 'user',)
