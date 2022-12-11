from rest_framework import serializers
from . import models


class HelloSerializer(serializers.Serializer):
    """ Serializes the name field for our API View """
    name = serializers.CharField(max_length = 10)

class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializes user profiles """

    class Meta:
        model = models.UserProfiles
        fields = ['id', 'email', 'name', 'password']
        extra_kwargs = {
        'password':{
        'write_only': True,
        'style':{
        'input_type':'password'
        }
        }
        }

    def create(self,validated_data):
        """ Creats and returns new user """

        user = models.UserProfiles.objects.create_user(
        name = validated_data['name'],
        email = validated_data['email'],
        password = validated_data['password']
        )

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """ Serializes profile feed items """

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_model', 'status', 'created')
        extra_kwargs = {'user_model':{'read_only' : True}}
