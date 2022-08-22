from rest_framework import serializers
from .models import *


# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserManager
#         fields = ("username", "password", "email",)
#         extra_kwargs = {
#             "password": {"write_only": True},
#             "password2": {"write_only": True},
#         }

#     def create(self, validated_data):
#         password = validated_data.pop("password", None)
#         password2 = self.initial_data.pop("password2", None)
#         instance = self.Meta.model(**validated_data)

#         if password is not None:
#             if password == password2:
#                 instance.set_password(password)
#                 instance.save()
#                 print("instance", instance)
#                 return instance

#             else:
#                 raise serializers.ValidationError(
#                     {"error": "Both password Do not match"}
#                 )


class restaurantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = restaurants
        fields = "__all__"