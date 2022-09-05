from rest_framework import serializers
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['userid','password','username','user_image',]