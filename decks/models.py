import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone

User = get_user_model()


class Deck(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_decks"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("deck_detail", args=[str(self.id)])


class Card(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name="cards")

    def __str__(self):
        return f"Q: {self.question} - A: {self.answer}"


class UserDeck(models.Model):
    deck = models.ForeignKey(
        Deck, on_delete=models.CASCADE, related_name="user_subscribed_decks"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subscribed_decks"
    )

    def get_absolute_url(self):
        return reverse("learning_deck_detail", args=[str(self.id)])


class UserCard(models.Model):
    class State(models.IntegerChoices):
        Learning = 1, "Learning"
        Review = 2, "Review"
        Relearning = 3, "Relearning"

    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="user_cards")
    user_deck = models.ForeignKey(
        UserDeck, on_delete=models.CASCADE, related_name="cards"
    )
    state = models.PositiveSmallIntegerField(choices=State.choices, default=None)
    step = models.IntegerField(default=None)
    stability = models.FloatField(default=None)
    difficulty = models.FloatField(default=None)
    due = models.DateTimeField(default=None)
    last_review = models.DateTimeField(default=None)

    def __str__(self):
        return f"{self.card} | Due: {self.due}"
