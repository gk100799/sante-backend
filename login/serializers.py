from rest_framework import serializers
from login.models import User

class LoginSerializer(serializers.ModelSerializer):
    class meta:
        model = User
        fields = ['username','password']