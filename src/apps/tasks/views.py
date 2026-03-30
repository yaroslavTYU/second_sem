from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Tasks
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import TaskSerlializer



class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all().order_by('-created_at')
    serializer_class = TaskSerlializer


    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    
    filterset_fields = ['is_done', 'title', 'description']
    ordering_fields = ['created_at', 'title', 'is_done']
    
    ordering = ['-created_at']
