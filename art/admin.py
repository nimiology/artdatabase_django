from django.contrib import admin

from art.models import Art


class ArtAdmin(admin.ModelAdmin):
    list_display = ('artist', 'title', 'year', 'type', 'location')
    search_fields = ('artist', 'title', 'year', 'type', 'location')
    ordering = ['artist', 'title']


admin.site.register(Art, ArtAdmin)
