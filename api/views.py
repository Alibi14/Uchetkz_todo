from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import TaskSerializer
from .models import Task
from .exceptions import TodoExecuteException
from uchetkz import tasks


class TaskViewSet(ListModelMixin,
                  RetrieveModelMixin,
                  UpdateModelMixin,
                  CreateModelMixin,
                  GenericViewSet,
                  DestroyModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def patch(self, request, *args, **kwargs):
        return self.update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)

    @action(detail=True, permission_classes=[IsAuthenticated, ], methods=['post'])
    def execute(self, request, pk):
        task = Task.objects.filter(id=pk, user=request.user)
        if not task.exists():
            raise TodoExecuteException
        task.update(status=True)
        tasks.email_send.delay(request.user.email)
        return Response({'status': "task is true (done)"})
