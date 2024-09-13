from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .models import Storage


# Create your views here.
@login_required
def home(request):
    is_manager = request.user.groups.filter(name='manager').exists()
    return render(request, 'mainapp/home.html', {'is_manager': is_manager})
    # return render(request, 'mainapp/home.html')

@login_required
def make_order(request):
    return render(request, 'mainapp/make_order.html')

@login_required
def view_orders(request):
    return render(request, 'mainapp/view_orders.html')

@login_required
def storage(request):
    items = Storage.objects.filter(user=request.user)
    return render(request, 'mainapp/storage.html', {'items': items})

@login_required
def profile(request):
    return render(request, 'mainapp/profile.html')

def main_page(request):
    return render(request, 'mainapp/main_page.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')  # Перенаправление после регистрации
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def manager_dashboard(request):
    if request.user.groups.filter(name='manager').exists():
        return render(request, 'mainapp/manager_dashboard.html')
    else:
        return redirect('home')  # Перенаправление, если пользователь не менеджер