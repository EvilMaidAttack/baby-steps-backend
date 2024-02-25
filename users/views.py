from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.contrib.auth import authenticate, login

from .models import AppUser
from .serializers import AppUserSerializer

class AppUserViewSet(ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer


class AppUserSignInView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email = email, password = password)

        if user:
            login(request, user)
            serializer = AppUserSerializer(user, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


