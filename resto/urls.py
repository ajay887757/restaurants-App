"""resto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView

)
from restaurents.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/jwt', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('CustomUserCreate/', CustomUserCreate.as_view(), name='CustomUserCreate'),
    path('login/', loginCustom.as_view(), name='loginCustom'),
    path('restaurants_list/', restaurants_list.as_view(), name='restaurants_list'),
    path('forgetotp/', forget.as_view(), name='forget'),
    path('forgetPassword/', forgetPassword.as_view(), name='forgetPassword'),
    path('logout/', Logout.as_view(), name='Logout'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),


]
