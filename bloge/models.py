from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from bloge.abastract_models import DateAbstractModel
from django.utils import timezone

class KategoriModel(models.Model):
    isim = models.CharField(max_length=30, blank=False, null=False)
    soyadı = models.CharField(max_length=100, default=timezone.now)
    slug = AutoSlugField(populate_from='isim', unique=True)
    
    class Meta:
        verbose_name = 'kategori'
        verbose_name_plural = 'kategoriler'
        db_table = 'kategori'

    def __str__(self):
        return self.isim
    
class YazilarModel(DateAbstractModel):
    resim = models.ImageField(upload_to='yazi_resimleri')
    baslik = models.CharField(max_length=50)
    icerik = RichTextField()
    slug = AutoSlugField(populate_from='baslik', unique=True)
    kategoriler = models.ManyToManyField(KategoriModel, related_name='yazi')
    yazar = models.ForeignKey('account.CustomUserModel', related_name='yazilar', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Yazı'
        verbose_name_plural = 'Yazılar'
        db_table = 'Yazi'

    def __str__(self):
        return self.baslik
    
class YorumModel(DateAbstractModel):
    yazan = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='yorum')
    yazi = models.ForeignKey(YazilarModel, on_delete=models.CASCADE, related_name='yorumlar' )
    yorum =models.TextField()

    class Meta:
        db_table = 'yorumlar'
        verbose_name = 'Yorum'
        verbose_name_plural = 'Yorumlar'

    def __str__(self):
        return self.yazan.username
    
class IletisimModel(models.Model):
    email = models.EmailField(max_length=250)
    isim_soyisim = models.CharField(max_length=150)
    mesaj = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'iletisim'
        verbose_name = 'İletişim'
        verbose_name_plural = 'İletişim'

    def __str__(self):
        return self.email

