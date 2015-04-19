# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('linuxci', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('idc', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('ctexte', models.TextField()),
                ('cdatecreation', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('idq', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('qtexte', models.TextField()),
                ('note', models.IntegerField(default=0)),
                ('qdatecreation', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reponse',
            fields=[
                ('idr', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('rtexte', models.TextField()),
                ('meilleur', models.BooleanField(default=False)),
                ('rdatecreation', models.DateTimeField(auto_now=True)),
                ('idq', models.ForeignKey(to='linuxci.Question')),
            ],
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
        migrations.RenameModel(
            old_name='Votes',
            new_name='Vote',
        ),
        migrations.RemoveField(
            model_name='commentaires',
            name='idr',
        ),
        migrations.RemoveField(
            model_name='commentaires',
            name='idu',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='idu',
        ),
        migrations.RemoveField(
            model_name='reponses',
            name='idq',
        ),
        migrations.RemoveField(
            model_name='reponses',
            name='idu',
        ),
        migrations.AlterField(
            model_name='vote',
            name='idr',
            field=models.ForeignKey(to='linuxci.Reponse'),
        ),
        migrations.DeleteModel(
            name='Commentaires',
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
        migrations.DeleteModel(
            name='Reponses',
        ),
        migrations.AddField(
            model_name='reponse',
            name='idu',
            field=models.ForeignKey(to='linuxci.User'),
        ),
        migrations.AddField(
            model_name='question',
            name='idu',
            field=models.ForeignKey(to='linuxci.User'),
        ),
        migrations.AddField(
            model_name='commentaire',
            name='idr',
            field=models.ForeignKey(to='linuxci.Reponse'),
        ),
        migrations.AddField(
            model_name='commentaire',
            name='idu',
            field=models.ForeignKey(to='linuxci.User'),
        ),
    ]
