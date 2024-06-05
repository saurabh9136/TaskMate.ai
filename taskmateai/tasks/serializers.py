from rest_framework import serializers
from tasks.models import Tasks, AIResponse

class AIResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIResponse
        fields = "__all__"
        
class TasksSerializer(serializers.ModelSerializer):
    ai_responses = AIResponseSerializer(many=True, read_only=True)
    class Meta:
        model = Tasks
        fields = "__all__"
        # depth = 1 to fetch all data 