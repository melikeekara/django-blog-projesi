from django.shortcuts import render,  get_object_or_404, redirect
from django.http import HttpResponse
from bloge.models import YazilarModel, KategoriModel, YorumModel
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from bloge.forms import IletisimForm
from bloge.models import IletisimModel
from django.contrib.auth import logout
from bloge.forms import YaziEkleModelForm
from bloge.forms import YaziGuncelleFormModel
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


def iletisim(request):
    form = IletisimForm()
    if request.method == 'POST':
        form= IletisimForm(request.POST)
        if form.is_valid():
            iletisim = IletisimModel()
            iletisim.email = form.cleaned_data['email']
            iletisim.isim_soyisim = form.cleaned_data['isim_soyisim']
            iletisim.mesaj = form.cleaned_data['mesaj']
            iletisim.save()
            return redirect('anasayfa')
    context = {
        'form': form
    }
    return render(request, 'pages/iletisim.html', context=context)

def anasayfa(request):
    sorgu =request.GET.get('sorgu')
    yazilar = YazilarModel.objects.order_by('-id')
    
    if sorgu:
        yazilar = yazilar.filter(
            Q(baslik__icontains=sorgu) | Q(icerik__icontains=sorgu)
        ).distinct()

    sayfa= request.GET.get('sayfa')

    paginator = Paginator(yazilar, 2)

    return render(request, 'pages/anasayfa.html', context={
        'yazilar': paginator.get_page(sayfa)
    })


def kategori(request, kategoriSlug):
    kategori = get_object_or_404(KategoriModel, slug=kategoriSlug)
    yazilar = kategori.yazi.all()
    print(yazilar)
    sayfa= request.GET.get('sayfa')
    paginator = Paginator(yazilar, 2)

    return render(request, 'pages/kategori.html', context={
        'yazilar': paginator.get_page(sayfa),
        'kategori_isim': kategori.isim
    })

@login_required(login_url='/')
def yazilarim(request):
    
    yazilar = request.user.yazilar.order_by('-id')
    sayfa= request.GET.get('sayfa')
    paginator = Paginator(yazilar, 5)

    return render(request, 'pages/yazilarim.html', context={
        'yazilar': paginator.get_page(sayfa),
    })

def detay(request, slug):
    yazi = get_object_or_404(YazilarModel, slug=slug)
    yorumlar = yazi.yorumlar.all()
    return render(request, 'pages/detay.html', context={
        'yazi': yazi,
        'yorumlar': yorumlar
    })

def cikis(request):
    logout(request)
    return redirect('anasayfa')

@login_required(login_url='/')
def yazi_ekle(request):
    form = YaziEkleModelForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        yazi = form.save(commit=False)
        yazi.yazar = request.user
        yazi.save()
        form.save_m2m()
        return redirect('detay', slug=yazi.slug)
    
    return render(request, 'pages/yazi_ekle.html', context={
       'form': form
    } )

@login_required(login_url='/')
def yazi_guncelle(request, slug):
    yazi = get_object_or_404(YazilarModel, slug=slug, yazar=request.user)
    form = YaziGuncelleFormModel(request.POST or None, files=request.FILES or None, instance=yazi)
    if form.is_valid():
        form.save()
        return redirect('detay', slug=yazi.slug)

    print(slug)
    return render(request, 'pages/yazi_guncelle.html', context={
        'form': form
    } )


def yazi_sil(request, slug):
    yazi = get_object_or_404(YazilarModel, slug=slug, yazar=request.user)
    yazi.delete()
    return redirect('yazilarim')

@login_required(login_url='/')
def sifre_degistir(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            kullanici = form.save()
            update_session_auth_hash(request, kullanici)
            messages.success(request, 'Şifreniz başarıyla güncellendi.')
            return redirect('sifre_degistir')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'pages/sifre_degistir.html', context={
        'form': form
    })

