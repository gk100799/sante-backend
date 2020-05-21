from django.shortcuts import render
from allaboutfeet.models import Products, Cart, ProductDetails, Brand, Style, Colors, Sizes, Orders
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
from django.db.models import Q



# @authentication_classes(())
# @permission_classes(())
@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def get_products(request):
    # import ipdb; ipdb.set_trace()
    context = Products.objects.all()
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
def addToCart(request,prodIdQuantitySize):
    # import ipdb; ipdb.set_trace()
    user = request.user
    prodId, quant, size = map(int,prodIdQuantitySize.split('_'))
    if Cart.objects.filter(user_id=user.id, pid=prodId, size=size).exists():
        inCart = Cart.objects.get(user_id=user.id, pid=prodId, size=size)
        inCart.quantity = inCart.quantity + 1
        inCart.save()
        return Response(data={'created':'false'},status=status.HTTP_201_CREATED)
    cart = Cart.objects.create(user_id=user.id, pid=prodId, quantity=quant, size=size)
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
            context['size'] = item.size
            context['id'] = item.id
            items.append(context)
            # context3 = json.loads(serializers.serialize('json', context))
            # items.append({
            #     'pid':
            # })
        return Response(data=items,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def filterProducts(request):
    filters = request.data
    objects = list(filters)
    products=[]
    brands = list(Brand.objects.values_list('bname', flat=True))
    style = list(Style.objects.values_list('sname', flat=True))
    color = list(Colors.objects.values_list('color', flat=True))
    if len(filters['brands']) == 0 : filters['brands'] = brands
    if len(filters['styles']) == 0 : filters['styles'] = style
    if len(filters['colors']) == 0 : filters['colors'] = color
    prods = ProductDetails.objects.filter(
        Q(bname__in=filters['brands']),
        Q(sname__in=filters['styles']),
        Q(color__in=filters['colors'])
    )
    context2 = json.loads(serializers.serialize('json', prods))
    for obj in context2:
        x=obj['fields']
        x['pid']=obj['pk']
        products.append(x)
    print(products)
    return Response(data=products, status=status.HTTP_200_OK)


@api_view(['POST'])
def updateCart(request):
    user = request.user
    prodId = request.data['pid']
    quantity = request.data['quantity']
    size = request.data['size']
    inCart = Cart.objects.get(user_id=user.id, pid=prodId, size=size)
    inCart.quantity = quantity
    inCart.save()
    return Response(status=status.HTTP_201_CREATED)

@api_view(['POST'])
def updateSizeCart(request):
    user = request.user
    prodId = request.data['pid']
    oldSize = request.data['oldSize']
    size = request.data['size']
    if Cart.objects.filter(user_id=user.id, pid=prodId, size=size).exists():
        inCart = Cart.objects.get(user_id=user.id, pid=prodId, size=size)
        inCart.quantity += 1
        Cart.objects.filter(user_id=user.id, pid=prodId, size=oldSize).delete()
        return Response(data={'updatedQuantity':'true'},status=status.HTTP_201_CREATED)
    inCart = Cart.objects.get(user_id=user.id, pid=prodId, size=oldSize)
    inCart.size = size
    inCart.save()
    return Response(status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def deleteCartItem(request, prodIdSize):
    user = request.user
    prodId, size = prodIdSize.split('_')
    Cart.objects.filter(user_id=user.id, pid=prodId, size=size).delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def orders(request):
    user = request.user
    data = request.data
    cart = list(Cart.objects.filter(user_id=user.id).delete())
    order = Orders.objects.create(cart)
    order.save()
    return Response(status=status.HTTP_201_CREATED)