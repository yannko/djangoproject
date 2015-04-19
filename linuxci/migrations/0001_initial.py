# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaires',
            fields=[
                ('idc', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('ctexte', models.TextField()),
                ('cdatecreation', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('idq', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('qtexte', models.TextField()),
                ('note', models.IntegerField(default=0)),
                ('qdatecreation', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reponses',
            fields=[
                ('idr', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('rtexte', models.TextField()),
                ('meilleur', models.BooleanField(default=False)),
                ('rdatecreation', models.DateTimeField(auto_now=True)),
                ('idq', models.ForeignKey(to='linuxci.Questions')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('idu', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=100, blank=True)),
                ('pseudo', models.CharField(max_length=50)),
                ('mdp', models.CharField(max_length=50)),
                ('level', models.IntegerField(default=1)),
                ('avatar', models.CharField(max_length=50, blank=True)),
                ('datecreation', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('idv', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('idr', models.ForeignKey(to='linuxci.Reponses')),
                ('idu', models.ForeignKey(to='linuxci.Users')),
            ],
        ),
        migrations.AddField(
            model_name='reponses',
            name='idu',
            field=models.ForeignKey(to='linuxci.Users'),
        ),
        migrations.AddField(
            model_name='questions',
            name='idu',
            field=models.ForeignKey(to='linuxci.Users'),
        ),
        migrations.AddField(
            model_name='commentaires',
            name='idr',
            field=models.ForeignKey(to='linuxci.Reponses'),
        ),
        migrations.AddField(
            model_name='commentaires',
            name='idu',
            field=models.ForeignKey(to='linuxci.Users'),
        ),
    ]
