
from django.contrib import admin
from django.urls import path
from allaboutfeet import views
from rest_framework import routers
 
# router = routers.DefaultRouter()
# #makes sure that the API endpoints work
# router.register(r'login/', views.user_login)
# admin.autodiscover()

urlpatterns = [
    path('product/<int:prodId>/',views.productDetails),
    path('products/', views.get_products),
    path('add-to-cart/<str:prodIdQuantity>/', views.addToCart),
    path('cart-items/', views.cartItems),
]
