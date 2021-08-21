from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import render
from .form import loginForm,registerForm
from django.contrib.auth import authenticate,login,logout

def login_view(request):
    form = loginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password= form.cleaned_data.get('password')
        user=authenticate(username=username,password=password)
        login(request,user)
        return redirect('home')
    return render(request,"accounts/forms.html",{'form':form, 'title':'Login'})

def register_view(request):
    form = registerForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=True)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        # user.is_staff = user.is_superuser = True
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('home')

    return render(request, "accounts/forms.html", {"form": form, 'title': 'Sign Up'})

def logout_view(request):
    logout(request)
    return redirect('home')
        
