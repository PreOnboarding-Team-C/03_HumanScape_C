import json
from utils.uploader import insert_data
from pathlib import Path
from rest_framework.views import APIView
from rest_framework.response import Response
import os
from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer


class TestAPIView(APIView):
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    def get(self, request):
        TEST_FILE_PATH = os.path.join(BASE_DIR, 'test_response.json')

        with open(TEST_FILE_PATH, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            test_data = json_data
        f.close()
        insert_data(test_data['data'])
        return Response(test_data)

    
class ProjectListAPIView(generics.ListAPIView):
    '''
    Assignee : 홍은비
    Reviewer : -
    '''
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    
class ProjectDetailAPIView(generics.RetrieveAPIView):
    '''
    Assignee : 홍은비
    Reviewer : -
    '''
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'number'
    
