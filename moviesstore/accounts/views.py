from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from . forms import CustomSignupForm
# Create your views here.
def signup(request):
    template_data ={}
    template_data['title'] = 'Sign up'
    if request.method == 'GET':
        template_data['form'] = CustomSignupForm()
        return render(request, 'accounts/signup.html',{'template_data':template_data})
    elif request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home.index')
        else:
            template_data['form'] = form
            return render(request, 'accounts/signup.html',{'template_data':template_data})
        
def loginacc(request):
    template_data = {}
    template_data['title'] = 'Login'
    template_data['form'] = AuthenticationForm()
    if request.method == 'GET':
        return render(request, 'accounts/login.html',{'template_data':template_data})
    elif request.method == 'POST':
        user = authenticate(request, username = request.POST['username'], 
                                password = request.POST['password'],)
        if user is None :
            template_data['error'] = 'The Username or Password is incorrect'
            return render(request, 'accounts/login.html',{'template_data':template_data})
        else:
            login(request, user)
            return redirect('home.index')
        
@login_required
def logoutacc(request):
    logout(request)
    return redirect('home.index')