from rest_framework import serializers
from .models import Task
from datetime import datetime
import pytz


class TaskSerializer(serializers.ModelSerializer):
    deadline = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S")

    def validate_deadline(self, data):
        now = datetime.now()
        now = pytz.utc.localize(now)
        if data < now:
            raise serializers.ValidationError('Нельзя создать таск в прошлом')
        return data

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'deadline', 'status')
        read_only_fields = ('status',)