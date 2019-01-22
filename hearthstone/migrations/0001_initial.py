# Generated by Django 2.1.1 on 2018-11-13 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
                ('playerClass', models.TextField(max_length=50)),
                ('cost', models.IntegerField(default=0)),
                ('img_url', models.TextField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),

        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.TextField(blank=False,max_length=255)),
                ('userFrom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('userTo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),

        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userFrom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('userTo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('value', models.IntegerField(default=0)),
            ],
        ),

        migrations.CreateModel(
            name='DeckCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='DeckHero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hearthstone.Deck')),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
                ('playerClass', models.TextField(default='NaN', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('attaquant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Attaquant', to=settings.AUTH_USER_MODEL)),
                ('defenseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Defenseur', to=settings.AUTH_USER_MODEL, null=True)),
                ('gagnant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('J1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='J1', to=settings.AUTH_USER_MODEL)),
                ('J2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='J2', to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit', models.IntegerField(default=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('troc', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Minion',
            fields=[
                ('card_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hearthstone.Card')),
                ('attack', models.IntegerField()),
                ('health', models.IntegerField()),
                ('rarity', models.TextField(blank=True, max_length=30)),
            ],
            bases=('hearthstone.card',),
        ),
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('card_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hearthstone.Card')),
            ],
            bases=('hearthstone.card',),
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=False,max_length=60)),
                ('description', models.TextField(blank=False, default='')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('updated', models.DateTimeField(auto_now=True, blank=True)),
                ('created', models.DateTimeField(auto_now=True, blank=True)),
            ],
        ),

        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=False,max_length=60)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hearthstone.Forum')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, blank=True)),
                ('created', models.DateTimeField(auto_now=True, blank=True)),
                ('closed', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True, max_length=10000)),
            ],
        ),

        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=False,max_length=60)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hearthstone.Topic')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, blank=True)),
                ('created', models.DateTimeField(auto_now=True, blank=True)),
                ('body', models.TextField(max_length=10000)),
            ],
        ),

        migrations.CreateModel(
            name='ProfanityWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=60)),
            ],
        ),

        migrations.CreateModel(
            name='ProfaneWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='usercard',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hearthstone.Card'),
        ),
        migrations.AddField(
            model_name='usercard',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='deckhero',
            name='hero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hearthstone.Hero'),
        ),
        migrations.AddField(
            model_name='deckcard',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hearthstone.Card'),
        ),
        migrations.AddField(
            model_name='deckcard',
            name='deck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hearthstone.Deck'),
        ),
    ]
