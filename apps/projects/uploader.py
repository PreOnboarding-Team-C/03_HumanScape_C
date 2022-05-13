from datetime import datetime
from apps.projects.models import Project


def insert_data(data):
    """
    Assignee : 홍은비
    Reviewer : 장우경
    """
    col = ['number', 'title', 'research_period', 'research_scope', 'research_case', \
        'research_responsible_institution', 'research_phase', 'total_subject_count',\
        'speciality']

    create_count = 0 # 추가된 데이터 건 수
    update_count = 0 # 업데이트된 데이터 건 수

    for rows in data:
        insert_period = 0
        insert_subject_count = 0

        # 연구기간 개월 수로 치환
        period = rows['연구기간']

        if not period:
            insert_period = 0
        elif "개월" in period and len(period)>2:
            insert_period = int(period[:period.index('개월')])
        elif "년" in period and len(period)>1:
            insert_period = int(period[:period.index('년')])*12

        # 전체목표연구대상자 수 int 형변환
        if rows['전체목표연구대상자수']:
            insert_subject_count = int(rows['전체목표연구대상자수'])
        
        project = {
            'number': rows['과제번호'],
            'title': rows['과제명'],
            'research_period': insert_period,
            'research_scope': rows['연구범위'],
            'research_case': rows['연구종류'],
            'research_responsible_institution': rows['연구책임기관'],
            'research_phase': rows['임상시험단계(연구모형)'],
            'total_subject_count': insert_subject_count,
            'speciality': rows['진료과']
        }
        
        _project = Project.objects.filter(number=rows['과제번호']).order_by('number').distinct().values(*col).first()

        if not _project: # 과제번호가 기존 데이터에 없는 번호라면 데이터 생성 
            Project.objects.create(**project)
            create_count+=1
        else:
            if project != _project: # 변경된 데이터라면 update
                del project['number']
                Project.objects.filter(number=rows['과제번호']).update(**project, updated_datetime=datetime.now())
                update_count+=1

    print(f"{'='*25} Project DATA UPLOADED SUCCESSFULLY {'='*25}")
    print(f"{'='*20} 생성된 데이터 수 : {create_count} 업데이트된 데이터 수 : {update_count} {'='*20}")
