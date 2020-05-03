
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken
from allaboutfeet.models import Products, Cart


@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    user = request.user
    # print(request.user.id)
    # serializer = UserSerializer(user)
    # print(user)
    # cursor = connection.cursor()
    # userId = User.objects.get(username=user).id
    # cartItems = Cart.objects.raw("SELECT count(*) as count FROM allaboutfeet_cart WHERE user_id=%s", [request.user])
    cartItems = Cart.objects.filter(user_id=user.id).count()
    print(cartItems)
    data = {
        "username": str(user),
        "cart": cartItems,
    }
    return Response(data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)