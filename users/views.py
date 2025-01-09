<<<<<<< HEAD
from .forms import UserRegisterForm
=======
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

>>>>>>> 1dd3b63334544b314dc8c0cadbd79859276d583e
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
<<<<<<< HEAD
        form = UserRegisterForm(request.POST)
=======
        form = UserCreationForm(request.POST)
>>>>>>> 1dd3b63334544b314dc8c0cadbd79859276d583e
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
        else:
<<<<<<< HEAD
            messages.error(request, 'There was an error with your submission.')
    else:
        form = UserRegisterForm()

=======
            # In case of an invalid form, render the form again
            messages.error(request, 'There was an error with your submission.')
    else:
        form = UserCreationForm()

    # Always render the form, whether it's POST or GET
>>>>>>> 1dd3b63334544b314dc8c0cadbd79859276d583e
    return render(request, 'users/register.html', {'form': form})



def login(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

<<<<<<< HEAD
=======
# messages.info 
# messages.success
>>>>>>> 1dd3b63334544b314dc8c0cadbd79859276d583e
