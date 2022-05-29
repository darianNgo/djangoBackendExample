# Response object takes any python or serialized data and renders as JSON data
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    # many to true because serializing multiple items
    # one item make it false
    serializer = ItemSerializer(items, many=True)
    # outputs as JSON data
    return Response(serializer.data)


@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# @api_view(['GET'])
# def getUsers(request):
#     # users = get_user_model().objects.all()
#     users = []
#     for user in User.object.all():
#         users.append(user.get)

#     print(users)
#     serializer = ItemSerializer(users, many=True)
#     return Response(serializer.data)
