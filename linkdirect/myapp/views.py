# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import UserProfile, Button
from .forms import UserProfileForm, ButtonForm
from django.contrib.auth.views import LoginView
from django.urls import reverse

def error_404_view(request, exception):
    return render(request, '404.html', status=404)
    
@login_required
def edit_profile(request, username):
    if request.user.username == username:
        profile = get_object_or_404(UserProfile, user=request.user)

        if request.method == 'POST':
            form = UserProfileForm(request.POST, request.FILES, instance=profile)
            button_form = ButtonForm(request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, 'Perfil atualizado com sucesso.')
                return redirect('profile', username=username)  # Redireciona para o perfil após salvar

            if button_form.is_valid():
                new_button = button_form.save(commit=False)
                new_button.user_profile = profile
                new_button.save()
                messages.success(request, 'Botão adicionado com sucesso.')

        else:
            form = UserProfileForm(instance=profile)
            button_form = ButtonForm()

        buttons = Button.objects.filter(user_profile=profile)
        return render(request, 'edit_profile.html', {
            'form': form,
            'button_form': button_form,
            'buttons': buttons
        })
    else:
        return redirect('home')  # Ou qualquer outra página que você deseje redirecionar

@login_required
def delete_button(request, button_id):
    button = get_object_or_404(Button, id=button_id)
    if button.user_profile.user == request.user:
        button.delete()
        messages.success(request, 'Botão removido com sucesso.')
    return redirect('edit_profile', username=request.user.username)

def profile(request, username):
    # Obtém o perfil do usuário com base no username fornecido
    user_profile = get_object_or_404(UserProfile, custom_url=username)

    # Verifica se o campo 'photo' do perfil está vazio
    if not user_profile.photo:
        return redirect('em_breve')  # Redireciona para a página inicial se não houver foto
    
    buttons = Button.objects.filter(user_profile=user_profile)

    return render(request, 'profile.html', {
        'profile': user_profile,
        'buttons': buttons,
    })

def home(request):
    username = request.user.username if request.user.is_authenticated else None
    return render(request, 'home.html', {'username': username})

class CustomLoginView(LoginView):
    def get_success_url(self):
        next_url = self.get_redirect_url()
        if next_url:
            return next_url
        return reverse('home')  # ou qualquer outra URL padrão

@login_required
def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')
    else:
        form = UserProfileForm()

    return render(request, 'create_profile.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect.')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')

def em_breve(request):
    return render(request, 'em-breve.html')
