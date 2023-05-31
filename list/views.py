import requests
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import UserForm, CommentaireForm, RepForm
from .forms import indexForm, indexChoice
from .models import Plat, HeuresTravail, Reponse, image
from .models import Restau, Commentaire, User
from django.db.models import Q
from django import template
from django.template.defaultfilters import stringfilter
from django.db.models import Sum,Max,Min,Avg
from django.template import Library
from django.urls import reverse
from django.template.loader import render_to_string
from geolite2 import geolite2
from geopy.geocoders import Nominatim
from decimal import Decimal


register = Library()
#@register.filter(name='convertTolist')


def previous(some_list, current_index):
    return some_list[int(current_index) - 1]

@register.inclusion_tag('list/rest_detail.html')
def nxt(some_list, current_index):
    return some_list[int(current_index) + 1]


def increment_var(var):
    return var+1

def plat_list(request,pk):
    rest = Restau.objects.get(id=pk)
    plats = rest.Plats.all()

    minimum = rest.Plats.aggregate(Min('prix'))
    maximum =  rest.Plats.aggregate(Max('prix'))
    moyenne =  rest.Plats.aggregate(Avg('prix'))
    cuisine =""
    plat=""
    allergies=""
    prix_min=0
    prix_max=0
    st=""
    allergie=list()
    if request.method == 'POST':
      cuisine = request.POST.get('cuisine',0)
      plat = request.POST.get('plat',0)
      allergies = request.POST['allergies']
      prix_min = request.POST['prix_min']
      prix_max = request.POST['prix_max']

      if prix_min and prix_max:
        plats = rest.Plats.filter(prix__range=(prix_min,prix_max))
      if allergies :
        allergie = allergies.split(',')
        plats = plats.filter(~Q(ingredients__contains=allergie[0]))
        del allergie[0]
        for i in allergie:
          plats = plats.filter(~Q(ingredients__contains=i))
      if cuisine:
        plats = plats.filter(Type_cuisine__contains=cuisine)
      if plat:
        plats = plats.filter(Q(categorie=plat))
    entree  = plats.filter(Q(Type_Plat='Salade') | Q(Type_Plat='Soupe') | Q(Type_Plat="Autre Entree"))
    dessert = plats.filter(Type_Plat="Dessert")
    principal = plats.filter(Type_Plat="Plat Principal")

    context = {'Restau': rest,'Plats': plats,'Entree': entree,'Dessert': dessert,
               'Principal': principal,'cuisine':cuisine,'plat':plat,'allergies':allergies,'prix_min':prix_min,
               'prix_max':prix_max, 'maximum':maximum['prix__max'] ,'minimum':minimum['prix__min'],
               'moyenne':int(moyenne['prix__avg']),'st':st
               }
    return render(request, 'list/plat_list.html', context)

def plat_list2(request,pk):
    rest = Restau.objects.get(id=pk)
    plats = rest.Plats.all()
    idu = request.session['idu']
    minimum = rest.Plats.aggregate(Min('prix'))
    maximum =  rest.Plats.aggregate(Max('prix'))
    moyenne =  rest.Plats.aggregate(Avg('prix'))
    cuisine =""
    plat=""
    allergies=""
    prix_min=0
    prix_max=0
    st=""
    allergie=list()
    if request.method == 'POST':
      cuisine = request.POST.get('cuisine',0)
      plat = request.POST.get('plat',0)
      allergies = request.POST['allergies']
      prix_min = request.POST['prix_min']
      prix_max = request.POST['prix_max']

      if prix_min and prix_max:
        plats = rest.Plats.filter(prix__range=(prix_min,prix_max))
      if allergies :
        allergie = allergies.split(',')
        plats = plats.filter(~Q(ingredients__contains=allergie[0]))
        del allergie[0]
        for i in allergie:
          plats = plats.filter(~Q(ingredients__contains=i))
      if cuisine:
        plats = plats.filter(Type_cuisine__contains=cuisine)
      if plat:
        plats = plats.filter(Q(categorie=plat))
    entree  = plats.filter(Q(Type_Plat='Salade') | Q(Type_Plat='Soupe') | Q(Type_Plat="Autre Entree"))
    dessert = plats.filter(Type_Plat="Dessert")
    principal = plats.filter(Type_Plat="Plat Principal")

    context = {'Restau': rest,'Plats': plats,'Entree': entree,'Dessert': dessert,
               'Principal': principal,'cuisine':cuisine,'plat':plat,'allergies':allergies,'prix_min':prix_min,
               'prix_max':prix_max, 'maximum':maximum['prix__max'] ,'minimum':minimum['prix__min'],
               'moyenne':int(moyenne['prix__avg']),'st':st,'idu':idu
               }
    return render(request, 'list/plat_list2.html', context)

def listing(request):
  cuisine = ""
  mot_cle=""
  tri=""
  resultat = Restau.objects.all()
  envoi = False
  if request.method == 'POST':
    envoi = True
    cuisine = request.POST.get('cuisine',0)
    mot_cle = request.POST['mot_cle']
    tri = request.POST.get('tri_par_etoile',0)
    if cuisine:
      resultat =  Restau.objects.filter(Q(Origine_cuisine=cuisine))
    if mot_cle :
      resultat = resultat.filter(Q(Adresse__contains=mot_cle)|Q(Nom__contains=mot_cle)|Q(Details__contains=mot_cle))
    if tri !=0 :
      resultat=resultat.order_by('-Votes')

  context = {'resultat': resultat,'cuisine':cuisine,'mot_cle':mot_cle,'tri':tri,'envoi':envoi}
  return render(request, 'list/listing.html', context)

def listing2(request):
  cuisine = ""
  mot_cle=""
  tri=""
  resultat = Restau.objects.all()
  envoi = False
  idu = request.session['idu']
  if request.method == 'POST':
    envoi = True
    cuisine = request.POST.get('cuisine',0)
    mot_cle = request.POST['mot_cle']
    tri = request.POST.get('tri_par_etoile',0)
    if cuisine:
      resultat =  Restau.objects.filter(Q(Origine_cuisine=cuisine))
    if mot_cle :
      resultat = resultat.filter(Q(Adresse__contains=mot_cle)|Q(Nom__contains=mot_cle)|Q(Details__contains=mot_cle))
    if tri !=0 :
      resultat=resultat.order_by('-Votes')

  context = {'resultat': resultat,'cuisine':cuisine,'mot_cle':mot_cle,'tri':tri,'envoi':envoi,'idu' :idu}
  return render(request, 'list/listing2.html', context)

def rest_detail(request, pk):
    rest = Restau.objects.get(id=pk)
    h = int('0' + rest.HeuresTrv.__str__())
    imgs = rest.images.all()
    idu = request.session['idu']
    user = User.objects.get(id=idu)
    # ht = rest.HeuresTrv,
    coordonnees = get_latitude_longitude(rest.Adresse)
    latitude = coordonnees[0]
    longitude = coordonnees[1]
    coms= Commentaire.objects.all().order_by('Date_pub')
    reps= Reponse.objects.all()
    #coms = Commentaire.objects.filter(Restau=rest).order_by('Date_pub')
    if request.method == 'POST':
        if 'comm' in request.POST:
            form = CommentaireForm(request.POST, request.FILES)
            if form.is_valid():
                v = int(request.POST.get('rating', 0))  # int(request.POST['rating'])
                # les données relatives au commentaire
                data = form.cleaned_data
                con = data['Contenu']
                c = Commentaire.objects.create(Restau=rest, User=user,
                                               Contenu=con, Date_pub=timezone.now())
                c.save()
                # les données relatives au restaurant
                rait = v*0.2
                rest.Votes += Decimal.from_float(rait)
                # les données relatives à l'image
                if form.cleaned_data.get("image"):
                    ima = form.cleaned_data.get("image")  # data['image']
                    imag = image.objects.create(image=ima)
                    imag.save()
                    rest.images.add(imag)
                rest.save()
                return redirect('rest_detail', pk=rest.id)

        elif 'rep' in request.POST:
            formrep = RepForm(request.POST)
            if formrep.is_valid():
                comid = request.POST['num'] #request.formrep['comf']
                com1 = Commentaire.objects.get(id=comid)
                data1 = formrep.cleaned_data
                con1 = data1['Contenu']
                c1 = Reponse.objects.create(User=user, Com=com1,
                                                Contenu=con1, Date_pub=timezone.now())
                c1.save()
                return redirect('rest_detail', pk=rest.id)
        elif 'com_id' in request.POST:
            comid = request.POST['com_id']  # request.formrep['comf']
            Comment = Commentaire.objects.get(id=comid)
            liked = False
            if Comment.likes.filter(id=user.id).exists():
                Comment.likes.remove(user)
                liked = False
            else:
                Comment.likes.add(user)
                liked = True
            return redirect('rest_detail', pk=rest.id)
        elif 'rep_id' in request.POST:
            repid = request.POST['rep_id']  # request.formrep['comf']
            reponse = Reponse.objects.get(id=repid)
            likedrep = False
            if reponse.replikes.filter(id=user.id).exists():
                reponse.replikes.remove(user)
                likedrep = False
            else:
                reponse.replikes.add(user)
                likedrep = True
            return redirect('rest_detail', pk=rest.id)
    else:
        formrep = RepForm()
        form = CommentaireForm(request.POST)

    context = {'Restau': rest,
               'Plats': rest.Plats.all(),
               'imgs': imgs,
               'form' : form,
               'formrep' : formrep,
               'coms': coms,
               'user':user,
               'reps':reps,
               'heuresT': rest.HeuresTrv,
               'hh': h,
               'heuresTrv': HeuresTravail.objects.filter(Q(pk=h)).values_list()[0],
               'loop_range': range(1, 8),
               'coordonnees': coordonnees,
               'latitude': latitude,
               'longitude': longitude,
               'zoom': coordonnees[2],
               'marker': coordonnees[3]
               }
    return render(request, 'list/rest_detail.html', context)

def get_latitude_longitude(adresse):
  L=list()
  geolocator = Nominatim(user_agent="djangoSite")
  location = geolocator.geocode(adresse)
  if location and location.latitude and location.longitude :
    L=[location.latitude, location.longitude,13,"/media/static/images/hat_marker.png"]
  else :
    L=[1,1,1,""]
  return L

def index(request):
    Restaus = Restau.objects.all()
    loc = Restaus_a_cote()
    Res_a_cote = Restau.objects.filter(Q(Adresse__contains=loc[0]) | Q(Adresse__contains=loc[1]),
                                       Q(Adresse__contains=loc[2]) | Q(Adresse__contains=loc[3]))
    choix = ""
    autre = ""
    resultat = {}
    valid = True
    message1 = ""
    message2 = ""
    # maps = folium.Map(location=[30.4110826, -9.5905125], zoom_start=15)
    if request.method == 'POST':
        choix = request.POST.get('dropdown', 0)
        autre = request.POST['autre']
        message1 = "Erreur 404"
        message2 = "Désolé, Aucun résultat ne correspond à votre recherche."
        if autre:
            resultat = Restau.objects.filter(Q(Adresse__contains=autre)).order_by('-Votes')
        elif choix:
            if choix == "1":
                # loc = Restaus_a_cote()
                # resultat = Restau.objects.filter(Q(Adresse__contains=loc[0])|Q(Adresse__contains=loc[1]),Q(Adresse__contains=loc[2])| Q(Adresse__contains=loc[3]))
                resultat = Res_a_cote
            elif choix != "1" and choix != 0:
                resultat = Restau.objects.filter(Adresse__contains=choix).order_by('-Votes')
        elif not choix and not autre:
            valid = False

    context = {'Res_a_cote': Res_a_cote, 'choix': choix, 'autre': autre, 'resultat': resultat,
               'valid': valid, 'message1': message1, 'message2': message2}
    return render(request, 'list/index.html', context)

def Restaus_a_cote():
  reader    =  geolite2.reader()
  #my_ip     =  requests.get('https://api.ipify.org').text
  location  =  reader.get("41.251.59.250") # reader.get(my_ip)
  if ('fr' in location['country']['names']):
    pays_fr   = (location['country']['names']['fr'])
  else:
    pays_fr   = (location['country']['names']['en'])
  if ('fr' in location['city']['names']):
    ville_fr  = (location['city']['names']['fr'])
  else:
    ville_fr  = (location['city']['names']['en'])

  pays_en   = (location['country']['names']['en'])
  ville_en  = (location['city']['names']['en'])
  L=list()
  L=[pays_fr,pays_en,ville_fr,ville_en]
  return L

def about(request):
    return render(request, 'list/about.html')

def about2(request):
    idu = request.session['idu']
    return render(request, 'list/about2.html', {'idu': idu})

def create_acount(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            nom = data['Nom']
            mailu = data['mail']
            mpass = data['MotPasse']
            form.save()
            user = User.objects.get(mail=mailu,Nom=nom, MotPasse=mpass)
            return redirect('index2',pk=user.id)
    else:
        form = UserForm()
    return render(request, 'list/create_acount.html', {'form': form})

def login(request):
    users = User.objects.all()
    if request.method == 'POST':
        passe = request.POST['password']
        mailu = request.POST['mail']
        user =User.objects.get(mail= mailu , MotPasse=passe)
        if user:
            return redirect('index2', pk = user.id)
            #return redirect('rest_detail2', pk=user.id)

    return render(request, 'list/index.html')

def logout(request):
    del request.session['idu']
    return redirect('index')

def index2(request,pk):
    Restaus = Restau.objects.all()
    user = User.objects.get(id=pk)
    request.session['idu'] = pk
    idu = request.session['idu']
    loc = Restaus_a_cote()
    Res_a_cote = Restau.objects.filter(Q(Adresse__contains=loc[0]) | Q(Adresse__contains=loc[1]),
                                       Q(Adresse__contains=loc[2]) | Q(Adresse__contains=loc[3]))
    choix = ""
    autre = ""
    resultat = {}
    valid = True
    message1 = ""
    message2 = ""
    # maps = folium.Map(location=[30.4110826, -9.5905125], zoom_start=15)
    if request.method == 'POST':
        choix = request.POST.get('dropdown', 0)
        autre = request.POST['autre']
        message1 = "Erreur 404"
        message2 = "Désolé, Aucun résultat ne correspond à votre recherche."
        if autre:
            resultat = Restau.objects.filter(Q(Adresse__contains=autre)).order_by('-Votes')
        elif choix:
            if choix == "1":
                # loc = Restaus_a_cote()
                # resultat = Restau.objects.filter(Q(Adresse__contains=loc[0])|Q(Adresse__contains=loc[1]),Q(Adresse__contains=loc[2])| Q(Adresse__contains=loc[3]))
                resultat = Res_a_cote
            elif choix != "1" and choix != 0:
                resultat = Restau.objects.filter(Adresse__contains=choix).order_by('-Votes')
        elif not choix and not autre:
            valid = False

    context = {'Restaus': Restaus,'user': user,'pk':pk,'Res_a_cote': Res_a_cote, 'choix': choix, 'autre': autre, 'resultat': resultat,
               'valid': valid, 'message1': message1, 'message2': message2,'idu':idu}
    return render(request, 'list/index2.html', context)

def meilleurs(request):
    Restaus = Restau.objects.all().order_by('-Votes')[:12:1]
    context={'Restaus':Restaus}
    return render(request,'list/meilleurs.html',context)
def meilleurs2(request):
    Restaus = Restau.objects.all().order_by('-Votes')[:12:1]
    idu = request.session['idu']
    context={'Restaus':Restaus, 'idu':idu}
    return render(request, 'list/meilleurs2.html', context)

def rest_detail2(request, pk):
    rest = Restau.objects.get(id=pk)
    h = int('0' + rest.HeuresTrv.__str__())
    imgs = rest.images.all()
    # ht = rest.HeuresTrv,
    coms= Commentaire.objects.all().order_by('Date_pub')
    reps= Reponse.objects.all()
    coordonnees = get_latitude_longitude(rest.Adresse)
    latitude = coordonnees[0]
    longitude = coordonnees[1]
    context = {'Restau': rest,
               'Plats': rest.Plats.all(),
               'imgs': imgs,
               'coms': coms,
               'reps':reps,
               'heuresT': rest.HeuresTrv,
               'hh': h,
               'heuresTrv': HeuresTravail.objects.filter(Q(pk=h)).values_list()[0],
               'loop_range': range(1, 8),
               'coordonnees': coordonnees,
               'latitude': latitude,
               'longitude': longitude,
               'zoom': coordonnees[2],
               'marker': coordonnees[3]
               }

    return render(request, 'list/rest_detail2.html', context)
