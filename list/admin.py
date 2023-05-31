from django.contrib import admin

from .models import Plat, HeuresTravail
from .models import Restau
from .models import User
from .models import Commentaire,Reponse
from .models import image

class PlatAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Plat._meta.fields]

class RestauAdmin(admin.ModelAdmin):
    list_display = ('id','Nom','Adresse','Origine_cuisine','Details','Votes','plats','photos','HeuresTravail')
    def plats(self, obj):
        return " - ".join([a.Nom for a in obj.Plats.all()])
    def photos(self, obj):
        return "-\n".join([a.image.name for a in obj.images.all()])

    def HeuresTravail(self, obj):
        return obj.HeuresTrv.pk
        #return self.select_related('HeuresTrv')
class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields]

class CommentaireAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Commentaire._meta.fields]
class ReponseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Reponse._meta.fields]
class imageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in image._meta.fields]

class HoraireTravailAdmin(admin.ModelAdmin):
    list_display = [field.name for field in HeuresTravail._meta.fields]

admin.site.register(Plat,PlatAdmin)
admin.site.register(Restau,RestauAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Commentaire,CommentaireAdmin)
admin.site.register(Reponse,ReponseAdmin)
admin.site.register(image,imageAdmin)
admin.site.register(HeuresTravail,HoraireTravailAdmin)

