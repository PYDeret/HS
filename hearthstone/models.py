from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


class Chat(models.Model):
    msg = models.TextField(max_length=255, blank=False)
    userFrom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userFrom_id') # Field name made lowercase.
    userTo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userTo_id')  # Field name made lowercase.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit = models.IntegerField(default=200)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Card(models.Model):
    name = models.TextField(max_length=30, blank=False)
    playerClass = models.TextField(max_length=50, blank=False , default="NaN")
    cost = models.IntegerField(default=0)
    img_url = models.TextField(max_length=255, blank=True)
    rarity = models.TextField(max_length=30, blank=True)

    def __str__(self):
        return self.name

class Deck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    cards = models.ManyToManyField(Card) #use json.dumps(var) to insert cards
    finished = models.BooleanField(default=False)


    def __str__(self):
        return self.title

class Follow(models.Model):
    userFrom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followFrom_id') # Field name made lowercase.
    userTo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followTo_id')  # Field name made lowercase.
    value = models.IntegerField(default=0)

class Hero(models.Model):
    name = models.TextField(max_length=30, blank=False)
    playerClass = models.TextField(max_length=50, blank=False, default="NaN")

    def __str__(self):
        return self.name
        

class Minion(Card):
    attack = models.IntegerField()
    health = models.IntegerField()

    def __str__(self):
        return self.name

class Room(models.Model):
    J1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='J1')
    J2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='J2', null=True)

class Spell(Card):

    def __str__(self):
        return self.name

class UserCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    playerClass = models.TextField(max_length=50, blank=False , default="NaN")
    cost = models.IntegerField(default=0)
    troc = models.IntegerField(default=0)
    
class Party(models.Model):
    attaquant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Attaquant')
    defenseur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Defenseur', null=True)
    gagnant = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.gagnant.username


class Forum(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True, default='')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title

    def num_posts(self):
        return sum([t.num_posts() for t in self.topic_set.all()])

    def last_post(self):
        if self.topic_set.count():
            last = None
            for t in self.topic_set.all():
                l = t.last_post()
                if l:
                    if not last: last = l
                    elif l.created > last.created: last = l
            return last

class Topic(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=10000, blank=True, null=True)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    closed = models.BooleanField(blank=True, default=False)

    def num_posts(self):
        return self.post_set.count()

    def num_replies(self):
        return max(0, self.post_set.count() - 1)

    def last_post(self):
        if self.post_set.count():
            return self.post_set.order_by("created")[0]

    def __unicode__(self):
        return unicode(self.creator) + " - " + self.title

class Post(models.Model):
    title = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    body = models.TextField(max_length=255)

    def __unicode__(self):
        return u"%s - %s - %s" % (self.creator, self.topic, self.title)

    def short(self):
        return u"%s - %s\n%s" % (self.creator, self.title, self.created.strftime("%b %d, %I:%M %p"))

    short.allow_tags = True


class ProfaneWord(models.Model):
    word = models.CharField(max_length=60)

    def __unicode__(self):
        return self.word
