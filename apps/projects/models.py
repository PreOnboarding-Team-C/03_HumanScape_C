from django.db import models

from utils.time_stamp import TimeStampModel


class Project(TimeStampModel):
    number = models.CharField(max_length=20)                              # 과제번호
    title = models.CharField(max_length=200)                              # 과제명
    research_period = models.PositiveSmallIntegerField()                  # 연구기간
    research_scope = models.CharField(max_length=30)                      # 연구범위
    research_case = models.CharField(max_length=30)                       # 연구종류
    research_responsible_institution = models.CharField(max_length=30)    # 연구책임기관
    research_phase = models.CharField(max_length=30)                      # 임상시험단계(연구모형)
    total_subject_count = models.PositiveSmallIntegerField()              # 전체목표연구대상자수
    speciality = models.CharField(max_length=30)                          # 진료과

    class Meta:
        db_table = 'projects'
