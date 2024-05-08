from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from config.settings import EMAIL_HOST_USER
from mailing.forms import MailingForm, MailForm, ClientForm
from mailing.models import Client, Mail, Mailing
from mailing.services import send_mailing


def index(request):
    """главная страница"""
    return render(request, 'mailing/index.html')


# CRUD для модели получателя-------------------------------------------------------------------------


class ClientListView(LoginRequiredMixin, ListView):
    """Список клиентов-получателей"""
    model = Client


class ClientDetailView(LoginRequiredMixin, DetailView):
    """Информация по конкретному получателю"""
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    """Создание нового получателя"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')

    def form_valid(self, form):
        """Привязка получателя к создавшему пользователю"""
        client = form.save()
        user = self.request.user
        client.user = user
        client.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    """Изменение получателя"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление получателя"""
    model = Client
    success_url = reverse_lazy('mailing:client_list')

# CRUD для модели письма-сообщения-------------------------------------------------------------------------


class MailListView(LoginRequiredMixin, ListView):
    model = Mail


class MailDetailView(LoginRequiredMixin, DetailView):
    """Информация о конкретном сообщении"""
    model = Mail


class MailCreateView(LoginRequiredMixin, CreateView):
    """Создание нового письма"""
    model = Mail
    form_class = MailForm
    success_url = reverse_lazy('mailing:mail_list')

    def form_valid(self, form):
        """Привязка сообщения к создавшему пользователю"""
        mail = form.save()
        user = self.request.user
        mail.user = user
        mail.save()
        return super().form_valid(form)


class MailUpdateView(LoginRequiredMixin, UpdateView):
    """Изменение сообщения"""
    model = Mail
    form_class = MailForm

    def get_success_url(self):
        return reverse('mailing:mail_view', args=[self.kwargs.get('pk')])


class MailDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление сообщения"""
    model = Mail
    success_url = 'mailing:mail_list'


# CRUD для модели рассылок-----------------------------------------------------------------------------

class MailingListView(LoginRequiredMixin, ListView):
    """Список всех рассылок"""
    model = Mailing


class MailingDetailView(LoginRequiredMixin, DetailView):
    """Информация о конкретной рассылке"""
    model = Mailing


class MailingCreateView(LoginRequiredMixin, CreateView):
    """Создание новой рассылки"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        """Привязка рассылки к создавшему пользователю"""
        mailing = form.save()
        user = self.request.user
        mailing.user = user
        mailing.save()
        return super().form_valid(form)

    # def form_valid(self, form):
    #     """Отправка рассылки"""
    #     mailing = form.save()
    #     mailing.status = 'создана'
    #     mailing.save()
    #     send_mailing()
    #     return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    """Изменение рассылки"""
    model = Mailing
    form_class = MailingForm

    def get_success_url(self):
        return reverse('mailing:mailing_view', args=[self.kwargs.get('pk')])


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление рассылки"""
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')
