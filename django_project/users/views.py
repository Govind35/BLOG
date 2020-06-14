from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  # inbuld function for form
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # for success msg
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)       #
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')        #to get data of username
            messages.success(request, f'Account created, Now you can login {username}! ')       # show success message
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required     # make sure that user is logged in else deny the permisssion to go for profile
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)        #form to be seen and previous is used for previous info in filds
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile) #form to be seen and previous is used for previous info in filds
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account is updated! ')       # show success message
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)        #form to be seen and previous is used for previous info in filds
        p_form = ProfileUpdateForm(instance = request.user.profile) #form to be seen and previous is used for previous info in filds
        
    context = {
        'u_form' : u_form,
        'p_form' : p_form

    }
    return render(request, 'users/profile.html', context)