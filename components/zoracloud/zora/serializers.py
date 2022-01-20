from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseCreateUserSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from .models import Profile, ProvisionResponse, User


class UserCreateSerializer(BaseCreateUserSerializer):
    class Meta(BaseCreateUserSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'email', 'first_name', 'last_name']


class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user_id', 'company', 'cpu', 'memory', 'gpu', 'number_of_disks', 'phone', 'membership', 'volume',
                  'user']


class Provision(serializers.ModelSerializer):
    class Meta:
        model = ProvisionResponse
        fields = ['provision_response']