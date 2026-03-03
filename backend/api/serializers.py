from rest_framework import serializers
from .models import Conversation

class QuestionSerializer(serializers.Serializer):
    question = serializers.CharField()

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = "__all__"