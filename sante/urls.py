
from django.contrib import admin
from django.urls import path, include
from login import views
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token 

# router = routers.DefaultRouter()
# #makes sure that the API endpoints work
# router.register(r'login/', views.user_login)
# admin.autodiscover()

urlpatterns = [
    path('/', admin.site.urls),
    # url('', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # path('login/',views.user_login),
    path('api/', include('allaboutfeet.urls')),
    path('login/', include('login.urls')),
    path('token-auth/', obtain_jwt_token),
]
