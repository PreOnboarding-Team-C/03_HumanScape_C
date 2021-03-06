from django.db import models

from utils.time_stamp import TimeStampModel


class Project(TimeStampModel):
    '''
    Assignee : 장우경, 홍은비
    Reviewer : 홍은비, 장우경
    '''
    number = models.CharField(max_length=20, primary_key=True, verbose_name='과제번호')
    title = models.TextField(verbose_name='과제명')
    research_period = models.PositiveSmallIntegerField(verbose_name='연구기간')
    research_scope = models.CharField(max_length=30, verbose_name='연구범위')
    research_case = models.CharField(max_length=30, verbose_name='연구종류')
    research_responsible_institution = models.CharField(max_length=30, verbose_name='연구책임기관')
    research_phase = models.CharField(max_length=30, verbose_name='임상시험단계(연구모형)')
    total_subject_count = models.PositiveIntegerField(verbose_name='전체목표연구대상자수')
    speciality = models.CharField(max_length=30, verbose_name='진료과')

    class Meta:
        db_table = 'projects'

    def __str__(self):
        return self.title
