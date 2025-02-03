from django.contrib import admin

from .models import Card, Deck, UserCard, UserDeck


class DeckAdmin(admin.ModelAdmin):
    list_display = ("title", "author")


class CardAdmin(admin.ModelAdmin):
    list_display = ("question", "answer")


class UserCardAdmin(admin.ModelAdmin):
    list_display = ("card_id", "due")


class UserDeckAdmin(admin.ModelAdmin):
    list_display = ("deck__title", "user_id")


admin.site.register(Deck, DeckAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(UserCard, UserCardAdmin)
admin.site.register(UserDeck, UserDeckAdmin)
