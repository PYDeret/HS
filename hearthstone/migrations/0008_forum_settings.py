# -*- coding: utf-8 -*-
import datetime
from django.db import migrations, models



class Migration(migrations.Migration):

    dependencies = [
        ('hearthstone', '0007_usercard_cost'),
    ]

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
            ('forum', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hearthstone.Forum')),
            ('topic', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hearthstone.Topic')),
            ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, blank=True, null=True)),
            ('updated', models.DateTimeField(auto_now=True, blank=True)),
            ('created', models.TextField(max_length=10000)),
            ('body', models.BooleanField(default=False)),
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
