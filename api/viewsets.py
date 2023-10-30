"""REST API viewsets"""

from rest_framework import viewsets, response
from . import models, serializers
from rest_framework.permissions import IsAuthenticated

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
        return response.Response(
            {"detail": f"user {user.username} created"}, status=201
        )

class ContactViewSet(viewsets.ModelViewSet):
    """Contac Viewset"""
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactModelSerializer

    def get_queryset(self):
        queryset = models.Contact.objects.filter(user=self.request.user)
        return queryset