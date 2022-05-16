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

### 어려웠던 점
*생성일과 수정일 관련하여 DateTimeField의 코드 override 적용하던 부분  
데이터 최초 저장시 생성일과 수정일이 0.0003초정도의 차이가 있어서 이를 해결해야 했습니다.  
DateTimeField의 데이터가 생성되거나 수정되는 부분들을 찾아가며 print를 찍어보며 데이터가 업데이트 되는 시간과 연관된 코드가 어떤 것인지 찾고자 했습니다.  
pre_save 메소드에서 value 값을 print 했을 때 밀리세컨 정도로 업데이트 값과 차이가 나서 다른 부분을 계속 찾아봤었는데 멘토님께서 그 부분의 밀리세컨 값을 0으로 하는게 어떻냐는 조언을 해주셔서 replace 함수 적용하여 "microsecond 값을 0"으로 변경시켜 위의 로직을 구현할 수 있었습니다.

</br>

## 홍은비

### 1. 수집된 전체 임상정보 리스트 API
1. 단순하게 list 정보만 출력하기 때문에, generics 라이브러리의 ListAPIView를 사용해 구현했습니다.

### 2. 수집된 특정 임상정보 API
1. url 에서 number(과제번호)를 문자열 형식으로 받아 generics 라이브러리의 RetrieveAPIView 에 lookup_field 를 설정하여 구현했습니다.

### 3. batch task 속 데이터 베이스 갱신 기능 구현
아래와 같은 로직으로 구현했습니다.
1. Open API 에서 받아온 데이터 중 '연구기간'을 개월 수로 치환한다.
2. '전체목표연구대상자수'를 정수형으로 변환한다.
3. 해당 데이터(Open API 에서 받아온 데이터) 의 과제번호가 테이블에 존재하지 않으면 새로 데이터를 추가한다.
4. 과제번호가 이미 존재한다면 데이터를 업데이트한다.

### 어려웠던 점
데이터 베이스 갱신 기능을 구현할 때, 처음에는 update_or_create 메소드를 이용해구현했습니다.

하지만 해당 메소드는 model 에 auto_now=True 옵션이 설정되어 있음에도 불구하고 update time 이 갱신되지 않았고, 이로 인해 최근 일주일내에 업데이트(변경사항이 있는) 된 임상정보 리스트 API 구현이 힘든 상황이었습니다.

각종 자료와 특히 django 공식 문서에서 auto_now 옵션에 대해 찾아본 결과, auto_now 옵션 혹은 auto_now_add 옵션 등은 django orm 의 기능이고, 데이터베이스에 직접 쿼리를 날리는 update 등과 같은 메소드는 적용이 되지 않는 것임을 알 수 있었습니다.

이후 save 를 사용하는 방법과 update 시 update time 을 현재 시간으로 직접 설정하는 방법 두 가지가 있음을 확인하고, 후자를 선택하여 수정 시간을 갱신할 수 있었습니다.

해당 이슈로 인하여 공식문서에 제 생각보다 훨씬 더 많은 정보가 있다는 것을 알 수 있었고, 데이터베이스 함수와 orm 을 분리하여 생각해볼 수 있었습니다.

</br>

## 진병수

### AWS EC2 배포 작업
이전에 했던 작업이라 오래 걸리지는 않았습니다.

### 어려웠던 점
백엔드만 배포하는건 처음이라 어떻게 서버를 유지시켜야 하는지 처음에 감이 안왔습니다.
tmux개념을 찾아보고 tmux를 이용해 서버를 유지시켰습니다.

</br>

## 김수빈

### Opendata API request 클래스 + crontab
일전에 공공데이터 포털에서 분석 과제를 해본 경험이 상대적인 이점으로 작용했으며, 아쉬운 점은 endpoint가 다른 경우 가변 인자로 인지하도록 작성하면 보다 효율적인 코드가 될 것이라고 생각합니다.

공공데이터 API 자체의 호출 난이도는 기상데이터와 비교하면 높은 편이 아니었기에 예전과 비교하면 간단하게 작성했으며, 오탈자로 발생했던 에러는 멘토님의 도움으로 발견할 수 있었습니다.

연간의 주기를 가지며 업데이트 되는 API가 과제로 주어졌기에, 굳이 잦은 주기로 설정할 필요가 없다고 판단했습니다. 따라서 만일의 경우를 대비해, 분기별 1회씩 업데이트 될 수 있도록 crontab을 작성했습니다.

### 어려웠던 점
crontab을 처음 사용해보았기에, 로그도 쌓인다는 것을 이해할 수 없었습니다. 검색 결과, 여타 스케줄링(git action 등)과 유사하게 진행됨을 알 수 있었습니다. 다만, crontab이 django에서 설정이 되었는데 terminal에서도 확인이 가능한 원리에 대해서는 아직까지 더 공부가 필요한 부분입니다.

</br>
