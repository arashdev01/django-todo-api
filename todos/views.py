# todos/views.py
from rest_framework import viewsets
#from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwnerOrReadOnly

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        