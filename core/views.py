from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import User, Kudos
from .serializers import KudosSerializer, UserSerializer
from .utils import can_give_kudos, kudos_remaining


class KudosViewSet(viewsets.ModelViewSet):
    serializer_class = KudosSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Kudos.objects.filter(receiver=self.request.user).order_by('-created_at')

    def create(self, serializer):
        receiver_id = self.request.data.get("receiver_id")
        message = self.request.data.get("message", "")
        sender = self.request.user

        try:
            receiver = User.objects.get(id=receiver_id)
        except User.DoesNotExist:
            return Response({"error": "Receiver not found."}, status=404)

        valid, msg = can_give_kudos(sender, receiver)
        if not valid:
            return Response({"error": msg}, status=400)

        kudos = Kudos.objects.create(sender=sender, receiver=receiver, message=message)
        return Response(self.get_serializer(kudos).data, status=201)

    @action(detail=False, methods=['get'], url_path='received')
    def received(self, request):
        kudos = Kudos.objects.filter(receiver=request.user).order_by('-timestamp')
        serializer = self.get_serializer(kudos, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='remaining')
    def remaining(self, request):
        remaining = kudos_remaining(request.user)
        return Response({"remaining": remaining})


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.exclude(id=self.request.user.id)

    @action(detail=False, methods=['get'], url_path='me')
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


