from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, ListView

from .models import Deck, UserDeck


class AllDeckListView(ListView):
    model = Deck
    context_object_name = "deck_list"
    template_name = "decks/all_decks.html"


class CreatedDeckListView(ListView):
    model = Deck
    context_object_name = "deck_list"
    template_name = "decks/created_decks.html"

    def get_queryset(self):
        return Deck.objects.filter(author=self.request.user)


class LearningDeckListView(ListView):
    model = UserDeck
    context_object_name = "deck_list"
    template_name = "decks/learning_decks.html"

    def get_queryset(self):
        return UserDeck.objects.filter(user=self.request.user)


class DeckDetailView(DetailView):
    model = Deck
    context_object_name = "deck"
    template_name = "decks/deck_detail.html"


class AddLearningDeckView(View):
    def post(self, request):
        deck_id = request.POST.get("deck_id")
        UserDeck.objects.create(user=request.user, deck_id=deck_id)
        return redirect(reverse("learning_decks"))
