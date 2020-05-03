from django.shortcuts import render
from allaboutfeet.models import Products, Cart
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.core import serializers
import json
from django.forms.models import model_to_dict
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from django.contrib.auth.models import User

# @authentication_classes(())
# @permission_classes(())
@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def get_products(request):
    # import ipdb; ipdb.set_trace()
    context = Products.objects.all()
    # products = []
    # for prod in context:
    #     products.append({
    #         'pid': prod.pid,
    #         'pname': prod.pname,
    #         'price': prod.price,
    #         'image': prod.imagename,
    #     })
    # print(products)
    # context2 = serializers.serialize('json', context)
    context3 = json.loads(serializers.serialize('json', context))
    context1 = []
    for obj in context3:
        x=obj['fields']
        x['pid']=obj['pk']
        context1.append(x)
    # print(context1)
    return Response(data=context1, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def productDetails(request, prodId):
    context = Products.objects.get(pid=prodId)
    # print(model_to_dict(context))
    return Response(data=model_to_dict(context), status=status.HTTP_200_OK)


@api_view(['POST'])
def addToCart(request,prodIdQuantity):
    # import ipdb; ipdb.set_trace()
    user = request.user
    prodId, quant = map(int,prodIdQuantity.split('_'))
    inCart = Cart.objects.get(user_id=user.id, pid=prodId)
    print(model_to_dict(inCart))
    if inCart:
        inCart.quantity = inCart.quantity + 1
        inCart.save()
        return Response(data={'created':'false'},status=status.HTTP_201_CREATED)
    cart = Cart.objects.create(user_id=user.id, pid=prodId, quantity=quant)
    cart.save()
    return Response(data={'created':'true'}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
# @permission_classes([])
def cartItems(request):
    # import ipdb; ipdb.set_trace()
    user = request.user
    cart = Cart.objects.filter(user_id=user.id)
    items = []
    if cart:
        for item in cart:
            context = dict()
            product = Products.objects.get(pid=item.pid)
            context = model_to_dict(product)
            context['quantity'] = item.quantity
            items.append(context)
            # context3 = json.loads(serializers.serialize('json', context))
            # items.append({
            #     'pid':
            # })
        return Response(data=items,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_200_OK)