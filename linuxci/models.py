from django.db import models

# Models : Utilisateur, Question, Reponse, Vote, Commentaire

# Model Utilisateur
class Utilisateur(models.Model):
	idu = models.CharField(max_length=20, primary_key=True)
	nom = models.CharField(max_length=50)
	prenom = models.CharField(max_length=100, blank=True)
	pseudo = models.CharField(max_length=50)
	mdp = models.CharField(max_length=50)
	level = models.IntegerField(default=1)
	avatar = models.CharField(max_length=50, blank=True)
	datecreation = models.DateField(auto_now_add=True)
	
# Model Question
class Question(models.Model):
	idq = models.CharField(max_length=20, primary_key=True)
	idu = models.ForeignKey(Utilisateur)
	qtexte = models.TextField()
	note = models.IntegerField(default=0)
	qdatecreation = models.DateTimeField(auto_now=True)
	
# Model Reponse
class Reponse(models.Model):
	idr = models.CharField(max_length=20, primary_key=True)
	idq = models.ForeignKey(Question)
	idu = models.ForeignKey(Utilisateur)
	rtexte = models.TextField()
	meilleur = models.BooleanField(default=False)
	rdatecreation = models.DateTimeField(auto_now=True)
	
# Model Vote
class Vote(models.Model):
	idv = models.CharField(max_length=20, primary_key=True)
	idr = models.ForeignKey(Reponse)
	idu = models.ForeignKey(Utilisateur)
	
# Model Commentaire
class Commentaire(models.Model):
	idc = models.CharField(max_length=20, primary_key=True)
	idr = models.ForeignKey(Reponse)
	idu = models.ForeignKey(Utilisateur)
	ctexte = models.TextField()
	cdatecreation = models.DateTimeField(auto_now=True)
	 
	