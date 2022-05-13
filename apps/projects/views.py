import datetime
import os
import json
from pathlib import Path
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import F, Q

from .models import Project
from .uploader import insert_data
from .serializer import ProjectSerializer


class DbUploaderAPIView(APIView):
    '''
    Assignee : 장우경
    Reviewer : 홍은비
    '''
    # DB Uploader용 
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

        # 아래의 2가지 조건으로 최근 일주일내 업데이트된 건인지 확인하여 리턴
        # 1. created_datetime과 updated_datetime 초 단위까지 구분해서 같지 않아야 한다.
        # 2. updated_datetime이 조회하는 시점 기준 시간상으로 일주일 내인지 확인한다.
        days = 7 
        diff_datetime = datetime.datetime.now() - datetime.timedelta(days=days)

        projects_queryset = Project.objects.filter(~Q(created_datetime=F('updated_datetime')),
                                                    updated_datetime__gte=diff_datetime)\
                                                    .order_by('number')[offset : offset+limit]

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
