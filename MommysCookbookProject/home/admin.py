from django.contrib import admin

from MommysCookbookProject.home.models import Note, Favorite


class NoteAdmin(admin.ModelAdmin):
    list_display = ('note_text', 'is_private', 'created_at', 'to_recipe', 'owner')
    list_filter = ('is_private', 'created_at')
    search_fields = ('note_text', 'to_recipe__title', 'owner__username')

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('to_recipe', 'owner')
    list_filter = ('to_recipe', 'owner')


admin.site.register(Note, NoteAdmin)
admin.site.register(Favorite, FavoriteAdmin)




