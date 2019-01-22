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
    path('change_troc/', views.change_troc, name='changeTroc'),
    path('forum/', views.forum, name='forum-detail'),
    url(r'^topic/(\d+)/$', views.topic, name='topic-detail'),
    url(r'^reply/(\d+)/$', views.post_reply, name='reply'),
    url(r'newtopic/(\d+)/$', views.new_topic, name='new-topic'),
    path('check/', views.check, name='check'),
    path('check/player/deck/<int:user_id>', views.checkPlayerDecks, name='checkPlayerDecks'),
    path('check/player/cards/<int:user_id>', views.checkPlayerCards, name='checkPlayerCards'),
    path('check/player/deck/cards/<int:user_id>/<int:deck_id>', views.checkPlayerDeckCards, name='checkPlayerDeckCards'),
    path('check/player/troc/<int:user_id>', views.getTrocCards, name='getTrocCards'),
    path('check/player/troc/choosecard/<int:usercard_id>', views.trocChooseCard, name='trocChooseCard'),
    path('check/player/troc/validate/<int:usercard_id>/<int:myusercard_id>', views.trocValidate, name='trocValidate'),
    path('follow/', views.change_follow, name='follow'),
    path('get_follow', views.get_follow, name="get_follow"),
    path('deck_choose/<str>', views.deck_choose, name="deck_choose"),
    path('choosebot/', views.choosebot, name="choosebot"),
    path('chooseother/', views.chooseother, name="chooseother"),
    path('chooseotherwin/<int:user1_id>/<int:user2_id>', views.chooseotherwin, name="chooseotherwin"),
]


