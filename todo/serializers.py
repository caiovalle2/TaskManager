from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import TasksModel

class UserSerializer(serializers.ModelSerializer):
    group = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'group']

    def get_group(self, obj):
        return obj.groups.first()
    
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasksModel
        fields = '__all__'