# memo-board

django 강의 실습용 프로젝트.

## Functions

로그인한 사용자만 담벼락에 글을 올릴 수 있다.

글 올리기 / 등록된 글 목록 보기 / 로그인 / 회원가입 / 프로필 보기 / 로그아웃의 기능이 있다.

## Usage

```bash
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

## ETC

- Jinja2 Template Engine을 사용하였다.
- `Python 3.5+`, `Django 1.11+` 환경에서 작성한 코드들이다.