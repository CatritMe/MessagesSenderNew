from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView, index, \
    MailCreateView, MailDetailView, MailUpdateView, MailDeleteView, MailListView

app_name = MailingConfig.name

urlpatterns =[
    path('', index, name='home'),
    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('client_view/<int:pk>', ClientDetailView.as_view(), name='client_view'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('update_client/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('delete_client/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
    path('mail_list', MailListView.as_view(), name='mail_list'),
    path('create_mail/', MailCreateView.as_view(), name='create_mail'),
    path('mail_view/<int:pk>/', MailDetailView.as_view(), name='mail_view'),
    path('update_mail/<int:pk>/', MailUpdateView.as_view(), name='update_mail'),
    path('delete_mail/<int:pk>/', MailDeleteView.as_view(), name='delete_mail'),
]