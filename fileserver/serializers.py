from rest_framework import serializers


class FileSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=225)
    file_name = serializers.CharField(max_length=225)
    file = serializers.FileField()
