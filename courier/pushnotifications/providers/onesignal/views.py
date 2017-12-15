from django.shortcuts import render

from rest_framework import viewsets, mixins, status, permissions
from rest_framework.response import Response

from .serializers import NotificationProfileSerializer
from .models import NotificationProfile


# Recieve a OneSignal Id and save it
class NotificationProfileViewSet(mixins.CreateModelMixin,
                                 viewsets.GenericViewSet):
    queryset = NotificationProfile
    serializer_class = NotificationProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # If the given id is already saved, just respond the client with an OK
        onesignal_id = request.data.get('onesignal_id')
        if NotificationProfile.objects.filter(user=request.user, onesignal_id=onesignal_id).exists():
            return Response({}, status=status.HTTP_200_OK)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
