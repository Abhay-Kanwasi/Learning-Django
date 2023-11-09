from django.contrib import admin
from .models import Song


class SongAdmin(admin.ModelAdmin):
    list_display = ['song_name', 'song_duration', 'written_by']


admin.site.register(Song, SongAdmin)