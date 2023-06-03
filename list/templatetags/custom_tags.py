from django import template
from django.utils import timezone
from time import gmtime, strftime
from django.utils.safestring import mark_safe

from list.models import User, Commentaire, Reponse

register = template.Library()

@register.simple_tag(takes_context=True)
def HeuresTravail(context):
    list=[]
    resultat=[]
    for elem in context['heuresTrv']:
        list.append(elem)
    jours=['','Lundi','', 'Mardi','',' Mercredi','','Jeudi','','Vendredi','','Samedi','','Dimanche']

    for i in range(1,15,2):
        if list[i] == list[i+1] :
            #resh = '<strong>%s</strong>%s' % (esc(first), esc(other))
            res = mark_safe(jours[i]+'<span style="float: right;"> Fermé toute la journée </span>')
            resultat.append(res)
        elif bool(list[i]) == 0:
            res = mark_safe(jours[i]+'<span style="float: right; color:#C70039;"> Ouvert toute la journée </span>')
            resultat.append(res)
        elif bool(list[i+1]) == 0:
            res = mark_safe(jours[i]+'<span style="float: right; color:#C70039;"> Ouvert toute la journée </span>')
            resultat.append(res)
        else:
            str = mark_safe(jours[i]+'<span style="float: right; color:#FFC300;  ">'+list[i].strftime('%I:%M %p')+' - '+list[i+1].strftime('%I:%M %p')+'</span>')
            resultat.append(str)
    return resultat

@register.simple_tag
def func(valeur):
    return valeur+1

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

@register.simple_tag
def greeting(some_string):
    return "Hello "+some_string

@register.simple_tag
def likedComment(user_id, comment_id):
    try:
        # tag_name is 'can_edit_report'
        #tag_name, user_id, comment_id = token.split_contents()
        # business logic here (can user like this comment?)
        user = User.objects.get(pk=user_id)
        com = Commentaire.objects.get(pk=comment_id)
        liked = False
        if com.likes.filter(id=user.id).exists():
            liked = True
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires two arguments")
    return liked
@register.simple_tag
def likedRep(user_id, rep_id):
    try:
        # tag_name is 'can_edit_report'
        #tag_name, user_id, comment_id = token.split_contents()
        # business logic here (can user like this comment?)
        user = User.objects.get(pk=user_id)
        rep = Reponse.objects.get(pk=rep_id)
        likedrep = False
        if rep.replikes.filter(id=user.id).exists():
            likedrep = True
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires two arguments")
    return likedrep