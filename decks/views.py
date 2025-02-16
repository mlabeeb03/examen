from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, ListView

from .models import Deck, UserCard, UserDeck


class AllDeckListView(ListView):
    model = Deck
    context_object_name = "deck_list"
    template_name = "decks/all_decks.html"


class CreatedDeckListView(LoginRequiredMixin, ListView):
    model = Deck
    context_object_name = "deck_list"
    template_name = "decks/created_decks.html"

    def get_queryset(self):
        return Deck.objects.filter(author=self.request.user)


class LearningDeckListView(LoginRequiredMixin, ListView):
    model = UserDeck
    context_object_name = "deck_list"
    template_name = "decks/learning_decks.html"

    def get_queryset(self):
        return UserDeck.objects.filter(user=self.request.user)


class DeckDetailView(DetailView):
    model = Deck
    context_object_name = "deck"
    template_name = "decks/deck_detail.html"


class AddLearningDeckView(LoginRequiredMixin, View):
    def post(self, request):
        deck_id = request.POST.get("deck_id")
        deck = Deck.objects.get(id=deck_id)
        with transaction.atomic():
            user_deck = UserDeck.objects.create(user=request.user, deck_id=deck_id)
            UserCard.objects.bulk_create(
                [UserCard(card=card, user_deck=user_deck) for card in deck.cards.all()]
            )
        return redirect(reverse("learning_decks"))


class LearningDeckDetailView(DetailView):
    model = UserDeck
    context_object_name = "deck"
    template_name = "decks/learning_deck_detail.html"
