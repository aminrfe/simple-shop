from django.urls import path, include
from auth.views import LogOutAPIView, CreateUserView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('create-user/', CreateUserView.as_view()), 
    path('login/', obtain_auth_token),
    path('logout/', LogOutAPIView.as_view()),
]