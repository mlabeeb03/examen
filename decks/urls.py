from django.urls import path

from .views import (
    AddLearningDeckView,
    AllDeckListView,
    CreatedDeckListView,
    DeckDetailView,
    LearningDeckDetailView,
    LearningDeckListView,
)

urlpatterns = [
    path("all_decks/", AllDeckListView.as_view(), name="all_decks"),
    path("created_decks/", CreatedDeckListView.as_view(), name="created_decks"),
    path("learning_decks/", LearningDeckListView.as_view(), name="learning_decks"),
    path("deck/<uuid:pk>/", DeckDetailView.as_view(), name="deck_detail"),
    path(
        "learning_deck/<int:pk>/",
        LearningDeckDetailView.as_view(),
        name="learning_deck_detail",
    ),
    path("add_learning_deck/", AddLearningDeckView.as_view(), name="add_learning_deck"),
]
