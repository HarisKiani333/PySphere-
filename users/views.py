from .forms import UserRegisterForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
        else:
            messages.error(request, 'There was an error with your submission.')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})



def login(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

