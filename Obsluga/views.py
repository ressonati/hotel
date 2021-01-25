from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from Obsluga.models import Pokoj2, Spa2

# Create your views here.


def index(request):
    return render(request, 'index.html')


def onas(request):
    return render(request, 'onas.html')


def pokoje(request):
    return render(request, 'pokoje.html')


def spa(request):
    return render(request, 'spa.html')


def infopokoje(request):

    p1 = Pokoj2()
    p1.img = 'pokoj1.jpg'
    p1.nazwa = 'Pokój nr 1 "Jak w domu"'
    p1.opis = 'blablabla'
    p1.cena = 3499

    p2 = Pokoj2()
    p2.img = 'pokoj2.jpg'
    p2.nazwa = 'Pokój nr 2 "W chmurach"'
    p2.opis = 'blablabla'
    p2.cena = 3699

    p3 = Pokoj2()
    p3.img = 'pokoj3.jpg'
    p3.nazwa = 'Pokój nr 1 "Kwiecisty raj"'
    p3.opis = 'blablabla'
    p3.cena = 3199

    pokoje = [p1, p2, p3]

    return render(request, 'infopokoje.html', {'pokoje': pokoje})


def infospa(request):

    s1 = Spa2()
    s1.nazwa = 'Masaż'
    s1.opis = 'blablablab'
    s1.cena = 20.99

    s2 = Spa2()
    s2.nazwa = 'Ruska bania'
    s2.opis = 'blablablab'
    s2.cena = 21.99

    s3 = Spa2()
    s3.nazwa = 'Sauna'
    s3.opis = 'blablablab'
    s3.cena = 22.99

    spa = [s1, s2, s3]

    return render(request, 'infospa.html', {'spa': spa})


def zaloguj(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Niepoprawne dane')
            return redirect('zaloguj')
    else:
        return render(request, 'zaloguj.html')


def rejestruj(request):
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Istenieje już konto o tym adresie email')
                return redirect('rejestruj')
            else:
                user = User.objects.create_user(username=email, email=email, password=password1)
                user.save()
                return redirect('zaloguj')
        else:
            messages.info(request, 'Podane hasła nie są identyczne')
            return redirect('rejestruj')
    else:
        return render(request, 'rejestruj.html')


def wyloguj(request):
    auth.logout(request)
    return redirect('/')

