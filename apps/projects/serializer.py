from rest_framework.serializers import ModelSerializer

from .models import Project


class ProjectSerializer(ModelSerializer):
    '''
    Assignee : 장우경
    Reviewer : -
    '''
    class Meta:
        model = Project
        fields = '__all__'
