import json
from rest_framework.views import APIView
from rest_framework.response import Response

class TestAPIView(APIView):
    def get(self, request):
        TEST_FILE_PATH = '/home/bruno/workspace/Humanscape/test_response.json'

        with open(TEST_FILE_PATH) as f:
            json_data = json.load(f)
            test_data = json_data

        # print(test_data)
        return Response(test_data)
