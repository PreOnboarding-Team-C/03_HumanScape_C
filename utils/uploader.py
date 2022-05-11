from apps.projects.models import Project

def insert_data(data):
    data_set = []

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

        data_set.append(
            Project(
                number = rows['과제번호'],
                title = rows['과제명'],
                research_period = insert_period,
                research_scope = rows['연구범위'],
                research_case = rows['연구종류'],
                research_responsible_institution = rows['연구책임기관'],
                research_phase = rows['임상시험단계(연구모형)'],
                total_subject_count = insert_subject_count,
                speciality = rows['진료과'],
            )
        )

    Project.objects.bulk_create(data_set)
    print(f"{'='*25} Project DATA UPLOADED SUCCESSFULLY {'='*25}")

