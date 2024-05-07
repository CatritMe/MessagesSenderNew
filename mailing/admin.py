from django.contrib import admin

from mailing.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)
    list_filter = ('name', 'email',)

