from django.contrib import admin
from CarsApp.models import MTCars, RankingItem, RankingLink  # importe seus modelos

# Modelos existentes
admin.site.register(MTCars)

# Registrando os modelos do ranking
@admin.register(RankingItem)
class RankingItemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'icone', 'descricao')

@admin.register(RankingLink)
class RankingLinkAdmin(admin.ModelAdmin):
    list_display = ('nome', 'link', 'item')
