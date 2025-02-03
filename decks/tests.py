from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()

from .models import Deck


class DeckTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(email="example@example.com")
        cls.deck = Deck.objects.create(
            title="Harry Potter",
            author=cls.user,
        )

    def test_deck_listing(self):
        self.assertEqual(f"{self.deck.title}", "Harry Potter")
        self.assertEqual(f"{self.deck.author.email}", "example@example.com")

    def test_deck_list_view(self):
        response = self.client.get(reverse("deck_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response, "decks/deck_list.html")

    def test_deck_detail_view(self):
        response = self.client.get(self.deck.get_absolute_url())
        no_response = self.client.get("/decks/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response, "decks/deck_detail.html")
