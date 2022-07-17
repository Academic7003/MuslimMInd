from dataclasses import fields
from rest_framework import serializers
from posts.models import PostModel, Creator


class PostSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = PostModel
        fields = "__all__"


class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = "__all__"

