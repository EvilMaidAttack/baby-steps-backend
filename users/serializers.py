from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import AppUser


class AppUserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = AppUser
        fields = ['id', 'first_name', 'last_name', 'email' , 'password']
        lookup_field = 'email'
        extra_kwargs = {'url': {'lookup_field': 'email'}}
    
    def create(self, validated_data):
        user = AppUser.objects.create_user(**validated_data)
        return user
        




