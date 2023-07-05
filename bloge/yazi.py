from django.db import models
from autoslug import AutoSlugField
from bloge.models import KategoriModel
from django.contrib.auth.models import User

class YazilarModel(models.Model):
    resim = models.ImageField(upload_to='yazi_resimleri')
    baslik = models.CharField(max_length=50)
    icerik = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    duzenlenme_tarihi = models.DateTimeField(auto_now=True)
    slug = models.SlugField(populate_from = 'baslik',unique=True)
    kategoriler = models.ManyToManyField('KategoriModel',related_name='yazi')
    yazar = models.ForeignKey(User, on_delete=models.CASCADE, related_name='yazilar')

    class Meta:
        verbose_name_plural = 'Yazı'
        verbose_name_plural = 'Yazılar'
        db_name = 'Yazi'