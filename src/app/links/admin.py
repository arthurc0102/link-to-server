from django.contrib import admin

from .models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('code', 'url', 'creator', 'create_at')
    list_filter = ('creator',)
    search_fields = ('code', 'url')
