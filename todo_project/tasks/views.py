from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request
from .models import Tasks
from .serializers import TaskSerlializer
from django.db.models.query import QuerySet


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerlializer
    def get_queryset(self):
        queryset = Tasks.objects.all()
        request: Request = self.request

        is_done = request.query_params.get('is_done')
        if is_done:
            if is_done.lower() == 'true':
                queryset = queryset.filter(is_done=True)
            elif is_done.lower() == 'false':
                queryset = queryset.filter(is_done=False)
        
        title = request.query_params.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title)

        created_at_data = request.query_params.get('created_at')
        if created_at_data:
            queryset = queryset.filter(created_at__date=created_at_data)

        sort_by = self.request.query_params.get('sort')
        if sort_by == 'oldest':
            queryset = queryset.order_by('created_at')  
        elif sort_by == 'newest':
            queryset = queryset.order_by('-created_at')  
        else:
            queryset = queryset.order_by('-created_at')  
        
        return queryset
