from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db.models import Sum
from django.db.models import Sum
from django.db.models import Max
from django.conf.locale.es import formats as es_formats
#from geoip import open_database
#from geolite2 import geolite2
#import requests

class User(models.Model):
    sex = [
        ('M', 'M'),
        ('F', 'F'),
    ]
    mail = models.EmailField(max_length=75)
    Nom = models.CharField(max_length=20)
    image = models.ImageField(upload_to='static\media', blank=True)
    sexe = models.CharField(max_length=2, default='M', choices=sex)
    MotPasse = models.CharField(max_length=20)

    # Adresse = models.CharField(max_length=50)
    def get_photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image
        elif self.sexe == 'M':
            return "/static/media/users/male-User.png"
        else:
            return "/static/media/users/Female-User.png"

    def __str__(self):
        return self.Nom


class HeuresTravail(models.Model):
    Lundi_ouverture = models.TimeField(blank=True, null=True)
    Lundi_cloture = models.TimeField(blank=True, null=True)
    Mardi_ouverture = models.TimeField(blank=True, null=True)
    Mardi_cloture = models.TimeField(blank=True, null=True)
    Mercredi_ouverture = models.TimeField(blank=True, null=True)
    Mercredi_cloture = models.TimeField(blank=True, null=True)
    Jeudi_ouverture = models.TimeField(blank=True, null=True)
    Jeudi_cloture = models.TimeField(blank=True, null=True)
    Vendredi_ouverture = models.TimeField(blank=True, null=True)
    Vendredi_cloture = models.TimeField(blank=True, null=True)
    Samedi_ouverture = models.TimeField(blank=True, null=True)
    Samedi_cloture = models.TimeField(blank=True, null=True)
    Dimanche_ouverture = models.TimeField(blank=True, null=True)
    Dimanche_cloture = models.TimeField(blank=True, null=True)

    def list_heures(self):
        list=[self.Lundi_ouverture,self.Lundi_cloture,self.Mardi_ouverture,self.Mardi_cloture,self.Mercredi_ouverture,self.Mercredi_cloture,self.Jeudi_ouverture,self.Jeudi_cloture,self.Vendredi_ouverture,self.Vendredi_cloture,self.Samedi_ouverture,self.Samedi_cloture,self.Dimanche_ouverture,self.Dimanche_cloture]
        return list

    def __str__(self):
        return "{}".format(self.pk)


"""	def __str__(self):
		return "Lundi:{} a {}\nMardi:{} a {}\nMercredi:{} a {}\nJeudi:{} a {}\nVendredi:{} a {}\nSamedi:{} a {}\nDimanche:{} a {}\n".format(self.Lundi_ouverture.es_formats.SHORT_DATETIME_FORMAT,
		self.Lundi_cloture.isoformat(timespec='minutes'),self.Mardi_ouverture.isoformat(timespec='minutes'),self.Mardi_cloture,self.Mercredi_ouverture,self.Mercredi_cloture,self.Jeudi_ouverture,self.Jeudi_cloture,self.Vendredi_ouverture,
		self.Vendredi_cloture,self.Samedi_ouverture,self.Samedi_cloture,self.Dimanche_ouverture,self.Dimanche_cloture)
	def __unicode__(self):
		return "Lundi:{} a {}\nMardi:{} a {}\nMercredi:{} a {}\nJeudi:{} a {}\nVendredi:{} a {}\nSamedi:{} a {}\nDimanche:{} a {}\n".format(self.Lundi_ouverture,
		self.Lundi_cloture,self.Mardi_ouverture,self.Mardi_cloture,self.Mercredi_ouverture,self.Mercredi_cloture,self.Jeudi_ouverture,self.Jeudi_cloture,self.Vendredi_ouverture,
		self.Vendredi_cloture,self.Samedi_ouverture,self.Samedi_cloture,self.Dimanche_ouverture,self.Dimanche_cloture)
"""


class Restau(models.Model):
    ORIGINE_CUISINE = [
        ('Cuisine Française', 'Cuisine Française'),
        ('Cuisine Marocaine', 'Cuisine Marocaine'),
        ('Cuisine Japonaise', 'Cuisine Japonaise'),
        ('Cuisine Italienne', 'Cuisine Italienne'),
        ('Cuisine Mexicaine', 'Cuisine Mexicaine'),
        ('Cuisine Grecque', 'Cuisine Grecque'),
    ]
    Nom = models.CharField(max_length=20)
    Adresse = models.CharField(max_length=50)
    Origine_cuisine = models.CharField(max_length=50, choices=ORIGINE_CUISINE)
    Details = models.TextField()
    Votes = models.DecimalField(max_digits=20, decimal_places=2)

    images = models.ManyToManyField('image', blank=True)
    Plats = models.ManyToManyField('Plat')
    HeuresTrv = models.OneToOneField(HeuresTravail, on_delete=models.CASCADE, blank=True, null=True,
                                     related_name='HeuresTrv')

    def get_photo_url(self):
        img: object = self.images
        return img

    def get_etoiles(self):
        max=Restau.objects.aggregate(max=Max('Votes'))['max']
        res = (self.Votes / max)*5
        list = []

        if res > 0:
            if res == 5:
                list=["complet.png","complet.png","complet.png","complet.png","complet.png"]
            else:
                for i in range(6):
                    if res > i + 1:
                        list.append("complet.png")
                    elif 0.15 < (res % 1) < 0.45:
                        list.append("quard.png")
                        break
                    elif 0.45 <= (res % 1) < 0.75:
                        list.append("moitie.png")
                        break
                    elif 0.75 <= (res % 1) < 0.9:
                        list.append("trois-quards.png")
                        break
            rest = 5 - len(list)
            if rest != 0:
                for i in range(len(list), 5):
                    list.append("vide.png")
        else :
            list=["vide.png","vide.png","vide.png","vide.png","vide.png"]
        return list

    def get_rating_value(self):
        max = Restau.objects.aggregate(max=Max('Votes'))['max']
        val = (self.Votes / max) * 5
        return '{:.1f}'.format(val)

    def __unicode__(self):
        return "{0}".format(self.Nom)

    def __str__(self):
        return self.Nom

    def get_premiere_image(self):
        list = self.images.all()
        return list


class Plat(models.Model):
	TYPE_CUISINE = [
		('Cuisine Traditionnelle', 'Cuisine Traditionnelle'),
		('Nouvelle Cuisine', 'Nouvelle Cuisine'),
		('Cuisine Exotique', 'Cuisine Exotique'),
		('Cuisine Gastronomique', 'Cuisine Gastronomique'),
		('Cuisine Moléculaire', 'Cuisine Moléculaire'),
	]
	TYPE_PLAT = [
		('Soupe', 'Soupe'),
		('Salade','Salade'),
		('Autre Entree','Autre Entree'),
		('Plat Principal', 'Plat Principal'),
		('Dessert', 'Dessert'),
	]
	CATEGORIE = [
		('Sans Gluten','Sans Gluten'),
		('Vegan', 'Vegan'),
		('Végétarien', 'Végétarien'),
		('Riche en protéines', 'Riche en protéines'),
		('Normal', 'Normal'),
	]
	Nom = models.CharField(max_length=75)
	Type_Plat = models.CharField(max_length=20,choices=TYPE_PLAT)
	ingredients = models.TextField()
	Type_cuisine = models.CharField(max_length=50,choices=TYPE_CUISINE,blank=True)
	image = models.ImageField(upload_to='static\media')
	prix = models.IntegerField()
	categorie = models.CharField(max_length=57,choices=CATEGORIE,blank=True)

	def ingredients_as_list(self):
		list=self.ingredients.split('-')
		firstUpper=list=[x.capitalize() for x in list]
		return firstUpper[:3]
	def all_ingredients_as_list(self):
		list=self.ingredients.split('-')
		firstUpper=list=[x.capitalize() for x in list]
		return firstUpper[:]
	def get_categorie(self):
		if self.categorie == "Normal":return ""
		else :return self.categorie
	def __unicode__(self):
		return "{0}:{0}".format(self.Nom,self.Type_Plat)
	def __str__(self):
		return self.Nom

class image(models.Model):
    image = models.ImageField(upload_to='static\media')
    nom = image.name
    def __unicode__(self):
        return "{0}".format(self.image)

    def __str__(self):
        return self.image.name
class Commentaire(models.Model):
    Restau = models.ForeignKey(Restau, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    #Likes = models.IntegerField(default=0)
    likes = models.ManyToManyField('User', related_name='likes')
    Contenu = models.TextField()
    Date_pub = models.DateTimeField(blank=True, null=True)

    # Reponse = models.ManyToManyField('self', blank=True)

    def publish(self):
        self.Date_pub = timezone.now()
        self.save()

    @property
    def total_likes(self):
        return self.likes.count()


class Reponse(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Com = models.ForeignKey(Commentaire, on_delete=models.CASCADE)
    replikes = models.ManyToManyField('User', related_name='replikes')
    Contenu = models.TextField()
    Date_pub = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.Date_pub = timezone.now()
        self.save()

    @property
    def total_likes(self):
        return self.replikes.count()



