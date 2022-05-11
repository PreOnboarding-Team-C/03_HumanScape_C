import os
import json
import django
from urllib.request import Request, urlopen

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.config.settings")
django.setup()

from utils.uploader import insert_data


def get_project_infos():
    apis = OpendataPortalAPIController()
    apis.set_url(apis.PERPAGE)
    insert_data(apis.get_json_data().get('data'))


class OpendataPortalAPIController:
    """
    Assignee : 김수빈
    Reviewer : 안병훈, 홍은비
    """
    url = f"https://api.odcloud.kr/api/3074271/v1/uddi:cfc19dda-6f75-4c57-86a8-bb9c8b103887"

    # init params
    API_KEY = os.environ.get("API_KEY")
    PAGE = 1
    PERPAGE = 10
    
    def __init__(self):
        self.URL = self.url + f"?page={self.PAGE}&perPage={self.PERPAGE}&serviceKey={self.API_KEY}"
        init_data = self.get_json_data()
        self.PERPAGE = init_data.get('totalCount')
        # self.__URL = self.URL(self.PERPAGE)

    def set_url(self, maxpage: int):
        self.URL = self.url + f"?page={self.PAGE}&perPage={str(maxpage)}&serviceKey={self.API_KEY}"

    def get_json_data(self):
        req = Request(self.URL)
        body = urlopen(req, timeout=60).read()
        return json.loads(body)


if __name__=='__main__':
    get_project_infos()
