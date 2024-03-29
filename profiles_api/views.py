from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from . import permissions
from . import models
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class HelloApiView(APIView):
    """ Test the API View """
    serializer_class = serializers.HelloSerializer
    def get(self, request, format = None):
        """ Returns a list of APIView features """
        an_apiview = [
        'uses HTTP methods as functions(get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your application logic',
        'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello!', 'an_apiview':an_apiview})

    def post(self, request):
        """ Create a Hello message with our name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'Message':'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update"""
        return Response({'Message':'PATCH'})

    def delete(self, request, pk=None):
        """delete an object"""
        return Response({'Message':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test the view set """

    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """ print a hello message and list an object """
        a_viewset = [
        'abc',
        'def',
        'ghi',
        'jkl',
        ]

        return Response({'message':'Hello!', 'a_viewset':a_viewset})

    def create(self, request):
        """ Create a Hello message with our name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        return Response({'HTTP Method':'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'HTTP Method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handle a partial update"""
        return Response({'HTTP Method':'PATCH'})

    def destroy(self, request, pk=None):
        """delete an object"""
        return Response({'HTTP Method':'DELETE'})


class UserProfileViewset(viewsets.ModelViewSet):
    """ Handling creating and updating user profiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfiles.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateObjectPermission,)
    filter_backends=(filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserloginAPIView(ObtainAuthToken):
    """ Handles login for users """

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ProfileFeedViewSet(viewsets.ModelViewSet):
    """ Handels creating, updating and deleting profile feed items """

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
    permissions.UpdateStatusPermission,
    IsAuthenticated
    )

    def perform_create(self,serializer):
        serializer.save(user_model=self.request.user)
