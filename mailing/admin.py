from django.contrib import admin

from mailing.models import Client, Mail, Mailing


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)
    list_filter = ('name', 'email',)


@admin.register(Mail)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('topic', 'text',)
    list_filter = ('topic',)


@admin.register(Mailing)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'status', 'periodicity')
    list_filter = ('name',)
