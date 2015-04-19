# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('linuxci', '0002_auto_20150419_2114'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Utilisateur',
        ),
    ]
