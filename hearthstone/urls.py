from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='app_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='app_logout'),
    path('party/', views.party, name='game'),
    path('buy-cards/', views.buyCards, name='buyCards'),
    path('my-cards/', views.myCards, name='myCards'),
    path('my-cards/delete/<int:card_id>/<str:rarity>', views.sellCard, name='sellCard'),
    path('my-decks/', views.myDecks, name='myDecks'),
    path('deck/<int:deck_id>', views.deck, name='deck'),
    path('deck/delete/<int:deck_id>', views.deleteDeck, name='deckDelete'),
    path('deck/update/<int:deck_id>', views.updateDeck, name='deckUpdate'),
    path('deck/create', views.createDeck, name='deckCreate'),
    path('deck/create/<int:hero_id>', views.createDeckByHero, name='createDeckByHero'),
    path('send_mmes/', views.send_mmes, name='sendMes'),
    path('get_mmes/', views.get_mmes, name='getMes'),
    path('forum/', views.forum, name='forum-detail'),
    url(r'^topic/(\d+)/$', views.topic, name='topic-detail'),
    url(r'^reply/(\d+)/$', views.post_reply, name='reply'),
    url(r'newtopic/(\d+)/$', views.new_topic, name='new-topic'),
]


