from rest_framework import serializers
from .models import Task, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields = ('id', 'title', 'description', 'due_date')
        extra_kwargs = {'due_date':{'format': '%Y-%m-%d'}}
    
