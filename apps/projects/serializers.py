from rest_framework.serializers import ModelSerializer
from .models import Project

class ProjectSerializer(ModelSerializer):
    '''
    Assignee : νμλΉ
    Reviewer : -
    '''
    class Meta:
        model = Project
        fields = '__all__'