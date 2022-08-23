from rest_framework import serializers
from .models import *


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = "__all__"

    def create(self, validated_data):
        # password = validated_data.pop("password", None)
        password =self.initial_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance



class restaurantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = restaurants
        fields = "__all__"