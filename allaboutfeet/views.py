from django.shortcuts import render
from allaboutfeet.models import Products
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from django.core import serializers
import json
from django.forms.models import model_to_dict


@api_view(['GET'])
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
    context2 = serializers.serialize('json', context)
    context3 = json.loads(context2)
    context1 = []
    for obj in context3:
        x=obj['fields']
        x['pid']=obj['pk']
        context1.append(x)
    # print(context1)
    return Response(data=context1, status=status.HTTP_200_OK)


@api_view(['GET'])
def productDetails(request, prodId):
    context = Products.objects.get(pid=prodId)
    # print(model_to_dict(context))
    return Response(data=model_to_dict(context), status=status.HTTP_200_OK)