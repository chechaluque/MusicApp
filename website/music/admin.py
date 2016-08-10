from django.contrib import admin
from .models import Album, Song


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('artist', 'album_title', 'genre')
    list_filter = ['artist']


class SongAdmin(admin.ModelAdmin):
    list_display = ('album', 'song_title', 'file_type', 'is_favorite')
    list_filter = ['album']
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
