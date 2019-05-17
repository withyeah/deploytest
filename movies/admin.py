from django.contrib import admin
from .models import Movie, Genre, Comment
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Movie._meta.get_fields()]
    list_display = ['title', 'release_date', 'genre',]
admin.site.register(Movie, MovieAdmin)   

class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
admin.site.register(Genre, GenreAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['movie', 'score', 'content',]
admin.site.register(Comment, CommentAdmin)
