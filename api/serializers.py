from rest_framework import serializers

from .models import Task, List

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'completed')

class ListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = List
        fields = ('title', 'updated_at')

class MyListSerializer(serializers.HyperlinkedModelSerializer):
    tasks = serializers.SerializerMethodField()
    class Meta:
        model = List
        fields = ('title','updated_at','id','tasks')

    def get_tasks(self,obj):
        tasks = Task.objects.filter(parrent=obj)
        return TaskSerializer(tasks, many=True).data