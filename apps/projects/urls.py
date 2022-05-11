from django.urls import path

from .views import ProjectListAPIView, ProjectDetailAPIView

urlpatterns = [
    # path('/test', TestAPIView.as_view()),
    path('', ProjectListAPIView.as_view()),
    path('/<str:number>', ProjectDetailAPIView.as_view()),
]
