from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# a view function takes a request and returns a response
#   aka request handler
#   some frameworks call it action
#   in django its called a view


def say_hello(request):
    return render(request, 'hello.html', {'name': 'Darian'})
