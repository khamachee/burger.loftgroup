from rest_framework import serializers

class WebHookSerializer(serializers.Serializer):
    sum = serializers.IntegerField()
    phone = serializers.CharField()
