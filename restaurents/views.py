from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .models import *
from django.db.models import Q
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from rest_framework.decorators import api_view
from .serializer import *
import math
from django.core.mail import send_mail

from django.contrib.auth import authenticate
import random



class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # serializer = CustomUserSerializer(data=request.data)
        # if serializer.is_valid():
        #     user = serializer.save()

        data=request.data
        user=data["username"]
        email=data["email"]
        password=data["password"]
        data_exist=NewUser.objects.filter(user_name=user)
        if data_exist.exists():
            return Response({"message":"user already exist"})

        usercreate=NewUser.objects.create(user_name=user,email=email,password=password)

        setattr(usercreate,"hello","Django4")
       
        data={
        "Status" :"User Created Successfully"
        }
        return Response(data, status=status.HTTP_201_CREATED)


class loginCustom(APIView):
    def post(self, request):
        data = request.data
        username = data.get("username")
        password = data.get("password")
        user_Data = NewUser.objects.filter(user_name=username,password=password)
        if user_Data.exists():
            if user_Data.first():
                RefrestTokenData = RefreshToken.for_user(user_Data.first())
                Token_Data = {
                    "access": str(RefrestTokenData.access_token),
                    "refresh": str(RefrestTokenData),
                    "Message": "Token Generated Successfully",
                }

                return Response(Token_Data, status=status.HTTP_200_OK)

        return Response(
            {"message": "Invalid user and password"}, status=status.HTTP_200_OK
        )

class restaurants_list(APIView):
    def get(self,request):
        restaurants_data=restaurants.objects.all()
        if restaurants_data.exists():
            serailizerd_data=restaurantsSerializer(restaurants_data,many=True).data
            
            return Response(serailizerd_data)


class forget(APIView):
    def post(self,request):
        data=request.data
        user_id=data["user_id"]
        digits = "0123456789"
        OTP = ""
        userData=NewUser.objects.filter(id=user_id)

        for i in range(6) :
            OTP += digits[math.floor(random.random() * 10)]
        
        if userData.exists():
            email=userData.first().email
            sendmail=forgrtpasswordfun(email,OTP=OTP)
        
        otpmodel=otp.objects.create(user_id=user_id,otpdata=OTP)

        return Response({"otp":OTP,"message":"otp send successfully"})
        

class forgetPassword(APIView):
    def post(self,request):

        data=request.data

        otpdata=data["otpdata"]
        user_id=data["user_id"]
        password=data["password"]
        otpdata=otp.objects.filter(user_id=user_id,otpdata=otpdata)
        if otpdata.exists():
            userdata=NewUser.objects.filter(id=user_id).first()
            userdata.password=password
            userdata.save()

            return Response({"Message":"Password Updated"})


def forgrtpasswordfun(
    email, subject="forget password",OTP=None
):
    message ="your otp is {}".format(OTP)
    user_email = [
        email,
    ]
    sender_email = settings.DEFAULT_FROM_EMAIL
    send_mail(
        subject,
        message,
        sender_email,
        user_email,
        fail_silently=True,
    )
    print("Mail Sended Successfully", send_mail)
    return True


class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)