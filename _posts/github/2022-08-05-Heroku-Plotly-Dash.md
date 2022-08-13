---
title: What is Heroku? How to use it?
layout: post
post-image:  ../assets/images/heroku.png
date: 2022-08-05 16:40:00
description: By default, Dash apps run on localhost and run with app.run_server(). However, there is an easy way to deploy your Dash app to a cloud environment. Dash uses Flask as its web framework and can be deployed anywhere Flask can be deployed. Options include Digital Ocean, PythonAnywhere, GCP, AWS, Azure, and more.
category: github
tags: GitHub Heroku Dash Plotly
permalink: "/blog/:title"
---


###### Source : [`Dr. Starson's Blog`](https://www.wenyanet.com/opensource/ko/6076863cf33f6b32cd7fba06.html)



# 1단계. Heroku 및 Git 설치

1. Heroku 계정을 엽니 다. 무료 계정은 [https://signup.heroku.com/dc](https://signup.heroku.com/dc)에서 사용할 수 있습니다 . 지침에 따라 사용자 이름과 암호를 얻습니다. 를 적어!
2. Heroku 계정에 로그인합니다. [https://dashboard.heroku.com/apps](https://dashboard.heroku.com/apps)로 이동합니다.
3. Python을 클릭하십시오. 다음 화면에서 설정을 선택합니다. Heroku CLI(명령 줄 인터페이스)를 다운로드하는 옵션이 나타납니다. 드롭 다운 목록에서 운영 체제를 선택하고 지침에 따라 유틸리티를 설치합니다. Git도 설치할 수있는 옵션이 있어야합니다.
4. git이 Heroku CLI와 함께 설치되지 않은 경우 [https://git-scm.com/downloads](https://git-scm.com/downloads)에서 직접 다운로드하고 운영 체제의 지침을 따를 수 있습니다.

	
# 2단계. virtualenv 설치

```
$ pip install virtualenv
```
 
Virtualenv를 사용하면 Python 및 앱에 필요한 모든 종속성을 포함하는 앱의 가상 환경을 만들 수 있습니다. 여기에는 특정 버전의 플롯, 대시 및 작동 할 것으로 알고있는 기타 라이브러리가 포함됩니다. 새로운 업데이트를 사용할 수있게되면 먼저 테스트 할 기회가있을 때까지 앱이 중단되지 않습니다!


# 3단계. 개발 폴더를 만들기

```
$ mkdir my_dash_app
$ cd my_dash_app
```

# 4단계. Git 초기화
```
$ git init
```
이렇게 하면 빈 git 저장소를 초기화합니다.

# 5단계. 가상 환경 생성, 활성화 및 채우기

1. 가상환경 구축 (가상환경 이름인 "venv"은 변경할 수 있습니다.)
```
$ python3 -m virtualenv venv
```


2. 가상환경 활성화
```
source venv/bin/activate
```

3. 가상환경에 dash 및 dependency 설치
```
$ pip install dash
$ pip install dash-auth
$ pip install dash-renderer
$ pip install dash-core-components
$ pip install dash-html-components
$ pip install plotly
...
```
 
4. 앱 배포를 위해 `gunicorn` 설치
```
$ pip install gunicorn
```

# 6단계. 개발폴더에 다음의 파일 추가
1. dash application 파일 작성: `app.py`(예시)
2. git에서 사용되며 push되지 않는 파일 식별 : `.gitignore`
```
*.pyc
```
3. 배포에 사용되는 `Procfile` 생성
```
web: gunicron app:server
```
4. Python 종속성을 설명하고 자동으로 생성되는 `requirements.txt` 생성
```
$ pip freeze > requirements.txt
```

# 7단계. Heroku 계정에 로그인
```
$ heroku login
```

# 8단계. Heroku app 생성, Git에 파일 추가 및 배포
1. Heroku app 생성 : 여기서 app name은 `example` 
```
$ heroku create example
Creating ⬢ example... done
https://example.herokuapp.com/ | https://git.heroku.com/example.git
```
`heroku create`는 `heroku apps:create`의 shorthand alias임.

2. Git 파일 추가 (`.gitignore`에 나열된 파일은 제외된 모든 파일은 git에 추가됨)
```
$ git add .
```

3. git commit
```
$ git commit -m 'message'
```

4. Heroku에 배포
```
$ git push heroku master
```
이때 다음과 같은 error message가 발생할 수 있음
```
error: src refspec master does not match any
error: failed to push some refs to 'https://git.heroku.com/example.git'
(venv) (base) ➜  my_dash_app git:(main) 
```
이 경우, 다음과 같이 명령하면 성공적으로 heroku 배포가 가능함
```
$ git push heroku HEAD:master
```

# 9단계. web에서 open app
`https://example.herokuapp.com`에서 app을 볼 수 있어야 함

# 10단계. 앱 업데이트
1. 새 패키지를 설치하는 경우
```
$ pip install newdependency
$ pip freeze > requirements.txt
```
2. 기존 패키지를 업데이트하는 경우
```
$ pip install dependency --upgrade
$ pip freeze > requirements.txt
```

# 11단계. markdown 파일에 dashboard를 추가
```
<iframe
  src="https://example.herokuapp.com"
  style="width:120%; height:700px; border: none; margin-left: -80px; margin-right: -80px;"
></iframe>
```

<style>
.responsive-iframe {
  position: relative;
  top: 20;
  left: 40;
  bottom: 0;
  right: 40;
  width: 100%;
  height: 100%;
  border: none;
}
</style>

<iframe class="responsive-iframe"
  src="https://uctest.herokuapp.com"></iframe>