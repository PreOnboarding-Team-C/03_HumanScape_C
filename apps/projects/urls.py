from django.urls import path

from .views import ProjectListAPIView, ProjectDetailAPIView, CheckUpdatedDataAPIView, DbUploaderAPIView


urlpatterns = [
    # path('/test', DbUploaderAPIView.as_view()),
    path('', ProjectListAPIView.as_view()),
    path('/list', CheckUpdatedDataAPIView.as_view()),   # 참고사항 : '/' + string 형태의 url 경우에는 아래의 '/<str:number>' url 위에 작성해야 404 에러가 발생하지 않습니다.
    path('/<str:number>', ProjectDetailAPIView.as_view()),
]
