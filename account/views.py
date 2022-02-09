from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, auth



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        pswd=request.POST['password']
        
        user= auth.authenticate(username=username, password=pswd)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            error='invalid credentials'
            return render(request,'login.html', {'error':error})
    else:
        return render(request, 'login.html')


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        pswd1 = request.POST['password1']
        pswd2 = request.POST['password2']
        error ="" 
        if pswd1==pswd2:
            if User.objects.filter(username=username).exists():
                error="Nome de usuário não disponível!"
                
            
            elif User.objects.filter(email=email).exists():
                error="Email já registrado!"
                
             
            else:
                user = User.objects.create_user(username=username, password=pswd1, email=email,
                                                first_name=first_name, last_name= last_name)
                user.save()
                print('User created')
                return redirect('login')
        else:
            error="As senhas não conferem" 
        
                
        return render(request, 'register.html', {'error':error})
 
   
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')