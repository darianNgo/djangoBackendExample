from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from rest_framework.decorators import api_view


# Create your views here.
# reference: https://github.com/cyber-hoax/login_auth_django_postgres
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request , user)

            # testing
            users = User.objects.all()
            print(users)

            return redirect('/home')    
        else:
            messages.info(request, 'invalid username or password')
            return redirect("/")
    else:
        return render(request,'index.html')


def register(request):
    if request.method == 'POST':

        email = request.POST['email']
        username = request.POST['username']
        password= request.POST['password']


        user = User.objects.create_user(username = username , password = password , email = email)
        user.save()
        print('user created')
        return redirect('/custom')

    return render(request,'register.html')

def custom(request):
    return render(request, 'custom.html')


def home(request):
    return render(request, 'home.html')

# @api_view(['GET'])
# def getUsers(request):
#     user = User
#     if user.is_authenticated():
#         usernames = []
#         users = User.objects.all()
#         for u in users:
#             usernames.append(u.get_username())
#         return usernames
#     else:
#         messages.info(request, 'please login')
        
    




