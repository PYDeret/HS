# Generated by Django 2.1.2 on 2018-11-13 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hearthstone', '0002_auto_20181113_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deckcard',
            name='card',
        ),
        migrations.RemoveField(
            model_name='deckcard',
            name='deck',
        ),
        migrations.RemoveField(
            model_name='deckhero',
            name='deck',
        ),
        migrations.RemoveField(
            model_name='deckhero',
            name='hero',
        ),
        migrations.AddField(
            model_name='deck',
            name='cards',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='deck',
            name='finished',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='DeckCard',
        ),
        migrations.DeleteModel(
            name='DeckHero',
        ),
    ]
