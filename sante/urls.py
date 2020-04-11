
from django.contrib import admin
from django.urls import path
from login import views
from rest_framework import routers
 
# router = routers.DefaultRouter()
# #makes sure that the API endpoints work
# router.register(r'login/', views.user_login)
# admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    # url('', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('login/',views.user_login),
]
