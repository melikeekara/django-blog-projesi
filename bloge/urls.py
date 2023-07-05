from django.urls import path, include
from bloge.views import iletisim, anasayfa
from bloge.views import kategori, yazilarim, detay, yazi_ekle, yazi_guncelle, yazi_sil, sifre_degistir
from bloge.views import cikis
from django.views.generic import TemplateView, RedirectView
from account.views import profil_guncelle, kayit
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('giris', auth_views.LoginView.as_view(
        template_name='pages/giris.html'
    ), name='giris'),
    path('', anasayfa, name='anasayfa'),
    path('iletisim', iletisim, name='iletisim'),
    path('hakkimda', TemplateView.as_view(
        template_name='pages/hakkimda.html'
    ), name='hakkimda'),
    path('yonlendir', RedirectView.as_view(
        url='https://www.google.com'
    ), name='yonlendir'),
    path('kategori/<slug:kategoriSlug>', kategori, name='kategori'),
    path('yazilarim', yazilarim, name='yazilarim'),
    path('detay/<slug:slug>', detay, name='detay'),
    path('cikis', cikis, name='cikis'),
    path('yazi-ekle', yazi_ekle, name='yazi-ekle'),
    path('yazi-guncelle/<slug:slug>', yazi_guncelle, name='yazi_guncelle'),
    path('yazi-sil/<slug:slug>', yazi_sil, name='yazi_sil'),
    path('sifre-degistir', sifre_degistir, name='sifre_degistir'),
    path('profil-guncelle', profil_guncelle, name='profil-guncelle'), 
    path('kayit', kayit, name='kayit'),

]
