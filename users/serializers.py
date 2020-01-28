from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 
            'first_name', 
            'last_name', 
            'email', 
            'gender',
            'ip_address',
        )