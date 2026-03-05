from rest_framework import serializers
from .models import Tasks


class TaskSerlializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks   
        fields = ['id', 'title', 'description', 'is_done', 'created_at']
        read_only_fields = ['id', 'created_at']
 