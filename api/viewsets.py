"""REST API viewsets"""

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from . import models, serializers

class UserViewSet(viewsets.ViewSet):
    """User sign up"""

    authentication_classes = []
    permission_classes = []
    serializer_class = serializers.UserModelSerializer

    def create(self, request):
        """Create new user action"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {"detail": f"User {user.username} created"}, status=201
        )

class ContactViewSet(viewsets.ModelViewSet):
    """Contac Viewset"""
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactModelSerializer

    def get_queryset(self):
        queryset = models.Contact.objects.filter(user=self.request.user)
        return queryset
    
    def create(self, request):
        """Create new contact"""
        validated_data = request.data
        user = models.User.objects.values('id').filter(username=self.request.user)[0]
        validated_data["user"] = user["id"]
        serializer = self.serializer_class(data=validated_data)
        if serializer.is_valid(raise_exception=True):
            contact = serializer.save()
            return Response({"detail": f"Contact {contact.first_name} {contact.middle_name} created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        item = get_object_or_404(models.Contact.objects.all(), pk=pk)
        validated_data = request.data
        user = models.User.objects.values('id').filter(username=self.request.user)[0]
        validated_data["user"] = user["id"]
        serializer = self.serializer_class(item, data=validated_data)
        if serializer.is_valid(raise_exception=True):
            contact = serializer.save()
            return Response({"detail": f"Contact {contact.first_name} {contact.middle_name} updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        item = get_object_or_404(models.Contact.objects.all(), pk=pk)
        validated_data = request.data
        user = models.User.objects.values('id').filter(username=self.request.user)[0]
        validated_data["user"] = user["id"]
        serializer = self.serializer_class(item, data=validated_data)
        if serializer.is_valid(raise_exception=True):
            contact = serializer.save()
            return Response({"detail": f"Contact {contact.first_name} {contact.middle_name} updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
