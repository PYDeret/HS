from django.contrib import admin

# Register your models here.
from .models import Deck, Hero, Minion, Spell, Party, Forum, Topic, Post, ProfaneWord

class ForumAdmin(admin.ModelAdmin):
    pass

class TopicAdmin(admin.ModelAdmin):
    list_display = ["title", "forum", "creator", "created"]
    list_filter = ["forum", "creator"]

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title", "creator"]
    list_display = ["title", "topic", "creator", "created"]

class ProfaneWordAdmin(admin.ModelAdmin):
    pass

admin.site.register(Deck)
admin.site.register(Minion)
admin.site.register(Hero)
admin.site.register(Spell)
admin.site.register(Party)
admin.site.register(Forum, ForumAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(ProfaneWord, ProfaneWordAdmin)