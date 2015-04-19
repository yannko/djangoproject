from django.contrib import admin
from linuxci.models import Utilisateur
from linuxci.models import Question
from linuxci.models import Reponse
from linuxci.models import Commentaire
from linuxci.models import Vote

admin.site.register(Utilisateur)
admin.site.register(Question)
admin.site.register(Reponse)
admin.site.register(Commentaire)
admin.site.register(Vote)