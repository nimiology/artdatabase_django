from django.contrib import admin

from art.models import Art


class ArtAdmin(admin.ModelAdmin):
    list_display = ('painter', 'title', 'year', 'type', 'location')
    search_fields = ('painter', 'title', 'year', 'type', 'location')
    ordering = ['painter', 'title']


admin.site.register(Art, ArtAdmin)
