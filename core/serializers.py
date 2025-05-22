from rest_framework import serializers
from .models import Kudos, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'organization']

class KudosSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    receiver = UserSerializer()

    class Meta:
        model = Kudos
        fields = ['id', 'sender', 'receiver', 'message', 'timestamp']
