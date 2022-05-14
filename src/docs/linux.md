# Linux (ubuntu)

## 설치 및 실행 방법
---
### Local 개발 및 테스트용
1. 해당 프로젝트를 clone 하고, 프로젝트 폴더로 들어간다.
```bash
    git clone https://github.com/PreOnboarding-Team-C/Humanscape.git
```
```bash
    cd Humanscape
```

2. Python version 체크 및 업그레이드
```bash
    python3 --version
    # 3.10 아닐 경우 아래의 방법으로 업그레이드
    sudo apt install software-properties-common -y
    sudo add-apt-repository ppa:deadsnakes/ppa -y
    sudo apt install python3.10 -y
    # 버전 확인
    sudo python3.10 --version
    # 정상적으로 진행되었다면 3.10.0 출력 확인
```

3. 가상 환경 설치, 생성 및 실행
```bash
    # venv 설치
    sudo apt-get install python3-venv
    # 가상환경 생성
    python3 -m venv 가상환경명
    # 가상환경 활성화 - 앞에 (가상환경명) 나오면 성공적으로 활성화
    source 가상환경명/bin/activate
    # 가상환경 종료하는 방법
    deactivate
```

4. Python 패키지 설치
```bash
    # 해당 프로젝트 루트 디렉토리에서 실행
    pip install -r requirements.txt
```

5. DB 생성
```bash
    mysql -u root -p
    # 위의 명령어 입력 후 비번 입력하여 접속
    # DB 생성
    CREATE DATABASE 데이터베이스명;
```

5. DB 생성 후 루트 디렉토리에 .env 생성하여 DB 정보 입력하여 연결한다.  
그 후 model의 변경사항을 DB에 반영한다.
```bash
    python manage.py makemigrations
    python manage.py migrate
```

6. 서버를 실행한다.
```bash
    python manage.py runserver 0.0.0.0:8000
```
