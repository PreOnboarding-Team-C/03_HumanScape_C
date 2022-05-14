# Humanscape

<div align="center">
  
  ![Python](https://img.shields.io/badge/Python-%20v3.8%20-blue.svg?&style=flat&logo=Python&logoColor=white&labelColor=abcdef&cacheSeconds=3600$logoWidth=60)
  ![MySQL](https://img.shields.io/badge/MySQL-%20v8.0%20-4479A1.svg?&style=flat&logo=MySQL&labelColor=ffffff&cacheSeconds=3600$logoWidth=80)
</div>

## Contexts
* [Guides](#guides)
* [API Documentation](#api-documentation)
* [Comments](#comments)

</br>

## Version 및 Tools
* Python 3.10
* Django 4.0
* MySQL

</br>

## Modeling
![HUMANSCAPE ERD  version2](https://user-images.githubusercontent.com/75561289/168232404-b1b48f64-a40c-4a7d-8321-b5b02354cb50.png)

<div align="center">

| 한글 컬럼명 | 영문 컬럼명 | 추가 설명 |
|------------|------------|-----|
| 과제번호 | number | PK |
| 과제명 | title | 길이 편차가 커서 확장성 고려하여 TextField로 결정 |
| 연구기간 | research_period | 기간에 따른 검색 기능 고려하여 PositiveSmallIntegerField로 결정 |
| 연구범위 | research_scope |  |
| 연구종류 | research_case |  |
| 연구책임기관 | research_responsible_institution |  |
| 임상시험단계(연구모형) | research_phase |  |
| 전체목표연구대상자수 | total_subject_count | 대상자수에 따른 검색 기능 고려하여 PositiveIntegerField로 결정 |
| 진료과 | speciality |  |
|  |  |  |
</div>

</br>

## Guides
해당 레포지토리를 clone한 뒤, 다음과 같이 `.env`파일을 프로젝트 폴더 최상단에 작성한다.

```shell
SECRET_KEY=$DJANGO_SECRET_KEY
API_KEY=$OPENDATA_API_KEY

# django.db.backends.mysql
MYSQL_DATABASE=$DATABASE_NAME
MYSQL_USER=$USER_NAME
MYSQL_PASSWORD=$PASSWORD
MYSQL_HOST=$HOST
MYSQL_PORT=$PORT_NO
```

가상 환경 설정 및 라이브러리 설치는 OS별 아래의 링크를 따르도록 한다.
* [MAC](./src/docs/mac.md)
* [WindowOS](./src/docs/windowos.md)
* [Linux](./src/docs/linux.md)

</br>

## API Documentation
![Python](https://img.shields.io/badge/Postman-%20orange.svg?&style=flat&logo=Postman&logoColor=red&labelColor=3950d&cacheSeconds=3600$logoWidth=60)

![img](./src/images/api_1.png "api 문서화 캡쳐본")
![img](./src/images/api_2.png "api 문서화 캡쳐본")
![img](./src/images/api_3.png "api 문서화 캡쳐본")

🌐[API Documentation Link](https://documenter.getpostman.com/view/12508509/Uyxhn7cA)

</br>

## 배포 가이드 및 주소 제공
[AWS EC2 적용](https://thundering-beef-7b9.notion.site/AWS-EC2-eac664ca95b644189ddea03886b2b91c)

[AWS 배포 및 tmux 활용하여 서버 실행](https://utopian-thistle-f43.notion.site/day13-05-13-AWS-tmux-4a0c1b52b79343f2b45963e94ae6a125)

## Comments

## 장우경
### 최근 일주일내에 업데이트(변경사항이 있는) 된 임상정보 리스트 API
아래의 로직을 먼저 생각한 후에 코드 작업을 진행했습니다.
1. 데이터 처음 저장시 created_datetime(생성일)과 updated_datetime(수정일)은 같을 것이다.
2. 만약 다르다면 생성된 후에 업데이트 되었을 것이다.
3. 그리고 조회하는 시점 기준으로 수정일이 일주일 이내이면 찾던 조건에 부합한다.

### 어려워던 점
*생성일과 수정일 관련하여 DateTimeField의 코드 override 적용하던 부분  
데이터 최초 저장시 생성일과 수정일이 0.0003초정도의 차이가 있어서 이를 해결해야 했습니다.  
DateTimeField의 데이터가 생성되거나 수정되는 부분들을 찾아가며 print를 찍어보며 데이터가 업데이트 되는 시간과 연관된 코드가 어떤 것인지 찾고자 했습니다.  
pre_save 메소드에서 value 값을 print 했을 때 밀리세컨 정도로 업데이트 값과 차이가 나서 다른 부분을 계속 찾아봤었는데 멘토님께서 그 부분의 밀리세컨 값을 0으로 하는게 어떻냐는 조언을 해주셔서 replace 함수 적용하여 "microsecond 값을 0"으로 변경시켜 위의 로직을 구현할 수 있었습니다.

</br>

## 홍은비

### 각자 맡은 API 또는 구현한 기능
1. something

### 어려워던 점
어려웠던 부분 서술

</br>

## 진병수

### 각자 맡은 API 또는 구현한 기능
1. something

### 어려워던 점
어려웠던 부분 서술

</br>

## 김수빈

### 각자 맡은 API 또는 구현한 기능
1. something

### 어려워던 점
어려웠던 부분 서술

</br>