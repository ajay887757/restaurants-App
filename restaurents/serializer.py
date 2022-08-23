from rest_framework import serializers
from .models import *


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ("user_name", "password", "email")
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)



class restaurantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = restaurants
        fields = "__all__"