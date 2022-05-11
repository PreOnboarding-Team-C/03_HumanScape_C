from django.urls import path

from .views import CheckUpdatedDataAPIView, TestAPIView


urlpatterns = [
    path('/test', TestAPIView.as_view()),
    path('/list', CheckUpdatedDataAPIView.as_view()),
]
