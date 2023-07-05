from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import ProfilDuzenlemeForm
from account.forms import KayitFormu
from django.contrib.auth import authenticate, login, logout
@login_required(login_url='/')
def profil_guncelle(request):
    if request.method == 'POST':
        form = ProfilDuzenlemeForm(request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil başarıyla güncellendi.')
            return redirect('profil_guncelle')
    else:
        form = ProfilDuzenlemeForm(instance=request.user)
        
    return render(request, 'pages/profil-guncelle.html', context={
        'form' : form
    })

def kayit(request):
    if request.method == 'POST':
        form = KayitFormu(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user =authenticate(username=username, password=password)
            login(request, user)
            return redirect('anasayfa')

    else:
        form = KayitFormu()

    return render(request, 'pages/kayit.html', context={
        'form' : form
    })