
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
    path('products/men', views.get_products),
    path('add-to-cart/<str:prodIdQuantitySize>/', views.addToCart),
    path('cart-items/', views.cartItems),
    path('products/filter/', views.filterProducts),
    path('cart-update', views.updateCart),
    path('delete-cart-item/<str:prodIdSize>', views.deleteCartItem),
    path('cart-size-update', views.updateSizeCart),
    path('orders', views.orders),
]
