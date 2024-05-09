from django.contrib import admin

from blogs.models import Blog


@admin.register(Blog)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', )
    list_filter = ('title', 'created_at',)