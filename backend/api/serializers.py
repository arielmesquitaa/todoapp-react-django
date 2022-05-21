from subprocess import CompletedProcess

from rest_framework import serializers
from todo.models import Todo


class TodoSerializer(serializers.Serializer):
    created = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()

    class Meta:
        db_table = Todo
        managed = True
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
        fields = ('id', 'title', 'memo', 'created', 'completed')
