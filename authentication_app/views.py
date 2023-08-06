from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import LoginForm

# Create your views here.
@login_required(login_url='login_view')
def home(request):

    # adicao de dados de usuario logado.
    contexto = {
        'username':request.user.username
    }
    return render(request, 'home.html', contexto)


def login_view(request):
    # quando o usuario tentar logar
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # checa se usuario existe
            user = authenticate(
                request, 
                username=username,
                password=password
            )

            # se usuario existir
            if user:
                login(request, user)
                return redirect('home')

    # quando a pagina for gerada/carregada
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login_view')