from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import MyUser
from django.contrib.auth.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True, validators=[UniqueValidator(queryset=MyUser.objects.all())])
    password = serializers.CharField(
        min_length=8,
        write_only=True, style={'input_type': 'password'})
    UserType = serializers.CharField(default="")
    Location = serializers.CharField(default="")

    class Meta:
        model = MyUser
        fields = ('username', 'password', 'UserType', 'Location')
        write_only_fields = ('password')

    def create(self, validated_data):
        user = super(CreateUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
