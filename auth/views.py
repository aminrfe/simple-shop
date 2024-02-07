from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from auth.serializers import CreateUserSerializer

class LogOutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()

        return Response({"message": "User logged out successfully"})

class CreateUserView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
    