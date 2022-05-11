import json
from utils.uploader import insert_data
from pathlib import Path
from rest_framework.views import APIView
from rest_framework.response import Response
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class TestAPIView(APIView):
    def get(self, request):
        TEST_FILE_PATH = os.path.join(BASE_DIR, 'test_response.json')

        with open(TEST_FILE_PATH, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            test_data = json_data
        f.close()
        # print(test_data['data'])
        insert_data(test_data['data'])
        # print(test_data['data'][0]['과제명'])
        return Response(test_data)
