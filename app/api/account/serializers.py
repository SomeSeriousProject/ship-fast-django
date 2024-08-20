from rest_framework import serializers


class GoogleIdTokenSerializer(serializers.Serializer):
    id_token = serializers.CharField()
