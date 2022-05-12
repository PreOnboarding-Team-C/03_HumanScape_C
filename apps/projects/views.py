import datetime
import os
import json
from pathlib import Path
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import F, Q

from .models import Project
from apps.projects.models import Project
from utils.uploader import insert_data
from .serializer import ProjectSerializer


class TestAPIView(APIView):
    '''
    Assignee : 장우경
    Reviewer : 홍은비
    '''
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    def get(self, request):
        TEST_FILE_PATH = os.path.join(self.BASE_DIR, 'test_response.json')

        with open(TEST_FILE_PATH, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            test_data = json_data
        f.close()
        insert_data(test_data['data'])
        return Response(test_data)


class CheckUpdatedDataAPIView(APIView):
    '''
    Assignee : 장우경
    Reviewer : 홍은비
    '''
    # days에 원하는 날짜 입력 => 최근 입력한 날짜 내의 업데이트 된 임상정보 리스트 리턴
    def get(self, request):
        offset = int(request.GET.get('offset', 0))
        limit = int(request.GET.get('limit', 10))
        
        days = 7 
        diff_datetime = datetime.datetime.now() - datetime.timedelta(days=days)

        projects_queryset = Project.objects.filter(~Q(created_datetime=F('updated_datetime')), updated_datetime__gte=diff_datetime).order_by('number')[offset : offset+limit]
        serializer = ProjectSerializer(projects_queryset, many=True)
        return Response(serializer.data, status=200)

    
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
