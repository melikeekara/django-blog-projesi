from django.contrib import admin
from bloge.models import KategoriModel
from bloge.models import YazilarModel
from bloge.models import YorumModel
from bloge.models import IletisimModel

admin.site.register(KategoriModel)

@admin.register(YazilarModel)
class YazilarAdmin(admin.ModelAdmin):
    search_fields = ('baslik', 'icerik')
    list_display = ('baslik', 'olusturulma_tarihi', 'duzenlenme_tarihi')

@admin.register(YorumModel)
class YorumAdmin(admin.ModelAdmin):
    list_display = ('yazan', 'olusturulma_tarihi', 'duzenlenme_tarihi')

@admin.register(IletisimModel) 
class IletisimAdmin(admin.ModelAdmin):
    list_display = ('email', 'olusturulma_tarihi')
    sesarch_fields = ('email')
