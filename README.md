<h1>데이터 CRUD 사이트</h1>
<hr>
<h2>★ 사용 언어, 프레임워크, 데이터베이스, 클라우드 플랫폼</h2>
<h4>● Frontend - HTML, CSS, Javascript</h4>
<h4>● Backend - Django(Python), SQLite3, AWS(Lightsail) </h4>
<hr>

<h2>★ 기능 소개</h2>
<h4>● Django에서 지원하는 회원가입 / 로그인 기능은 Admin 암호 입력해야만 실행</h4>
<h4>● 데이터 CRUD (생성, 읽기, 수정, 삭제)</h4>
<h4>● 데이터 등록 시 파일(~DFU.zip)에 대해 자동으로 CRC32 계산</h4>
<h4>● 삭제 및 수정 등, 기타 버튼 클릭 시 비밀번호 요구</h4>
<h4>● 선택한 데이터 미리보기 기능 모달창 형태로 show (최종화면 + 선택한 해당 데이터)</h4>
<h4>● 데이터 파일 다운로드 url에서 다운로드 가능</h4>
<h4>● 로그인 되어 있지 않으면 기본 index 페이지 보이지 않음</h4>
<hr>

<h2>★ 사이트 주소</h2>
<h4>[13.124.142.118](13.124.142.118)</h4>
<p>※ Admin 암호 입력해야 이용 가능</p>
<hr>

<h2>★ 구현 과정</h2>
<h3>1일차</h3>
<p>● DFU 파일 관리 사이트(안) 내용 숙지 및 앞으로의 작업 계획 구상</p>
<p>● Django로 작업 결정 및 공부(구글링, 유튜브, 등 ...)</p>
<hr>

<h3>2일차</h3>
<p>● CRUD 게시판 Javascript로 구현, 그러나 이는 Frontend 단에서만 작동</p>
<p>● 따라서 Backend의 기능을 위해 데이터베이스 (SQLite3) 필요</p>
<hr>

<h3>3일차</h3>
<p>● Django의 SQLite3로 DB 저장 및 불러오기 성공</p>
<hr>

<h3>4일차</h3>
<p>● CRUD 기능 모두 구현 완료</p>
<hr>

<h3>5일차</h3>
<p>● models.py에 DateTimeField, FileField 생성</p>
<p>● DB 파일 추가 가능, request.FILES 다루기</p>
<p>● CRC32 계산 알고리즘을 Javascript로 구현</p>
<hr>

<h3>6일차</h3>
<p>● settings.py에 login/logout redirect url 생성</p>
<p>● views.py에 register함수(UserCreationForm) 생성</p>
<p>● register.html과 registration폴더에 login.html 생성하여 회원가입 / 로그인 마무리</p>
<hr>

<h3>7일차</h3>
<p>● models.py에 또 다른 class 만들고 변수들 똑같이 각각 생성</p>
<p>● 선택한 데이터만 따로 추출하여 새롭게 출력하기 ← 선택한 데이터를 이중리스트로 변환한 후 저장, 그 후 checkbox name={{displayst.id}}가 submit 되면 이중리스트 for문, if 문으로 내부리스트(i)들의 0번째 인덱스가 {{display.id}}와 같으면 아까 그 다른 class의 변수들을 모두 새로운 리스트에 append하고 html에 출력</p>
<p>● 암호 설정하여 보안 기능 구현 ← Javascript로 prompt창 만들고 암호 맞으면 form의 onsubmit을 True로 설정해서 내보내기, 틀리면 아무 변화없이 False</p>
<hr>

<h3>8일차</h3>
<p>● 미리보기 모달창, 최종화면 생성</p>
<p>● 클래스모델 하나 더 만듬 (미리보기 DB 필요)</p>
<p>● 미리보기의 마지막 인덱스의 value 값들을 따로 저장</p>
<p>● 장고에 기본 탑재된 로그인, 로그아웃 기능과 장고 템플릿 문법을 통해 로그인 할 경우에만 원하는 UI 띄우도록 설정</p>
<p>● 깃허브 올리기</p>
<hr>

<h3>9일차</h3>
<p>● 미리보기를 최종화면 + (대기하기한 해당 데이터)으로 변경</p>
<p>● 미리보기 및 최종화면에 삭제 기능 추가</p>
<p>● 번호 삭제하고 버튼 순서 매기기</p>
<p>● 삭제하고 나서 기존 다른 버튼 누르면 오류 발생하여, 해결 ← views.py에서 index.html을 render하는 함수가 총 3개인데, stdisplay가 넘겨주는 값들 중 몇몇을 stdelete와 stdelete2는 넘겨주지 않았기 때문에 발생했던 것</p>
<p>● 회원가입 페이지에서 로그인페이지 url로 이동하도록 구현</p>
<p>● register 페이지에서 Admin 암호 입력해야 회원가입 할 수 있도록 구현</p>
<hr>

<h3>10일차</h3>
<p>● PuTTY generator로 pem파일을 ppk로 변환</p>
<p>● 깃허브에 key 등록</p>
<p>● PuTTY configurator로 Lightsail SSH 접속</p>
<p>● uwsgi랑 nginx로 서버 배포 성공</p>
<p>● 웹 글씨 키우기 + 대기하기 누를 시 이벤트 + 메인페이지에 기능 안내 + 최종화면 각 행 맨 앞에 $ 표시</p>
<p>● 로그인해야 화면 보이도록 모두 설정</p>
<hr>

<h3>11일차</h3>
<p>● 모든 페이지 구글폰트 적용</p>
<p>● css 꾸미기 및 통일</p>
<p>● Javascript의 querySelectorAll과 forEach, addEventListener, event.target.setAttribute를 통해 for 문 안에 있는 각각의 속성들을 클릭했을 시 이벤트 처리 완료</p>
<p>● 서버 배포한 웹 수정 ← sudo rm -rf DFU-site로 경로 초기화 후 git clone git@github.com:seungjun222/DFU-site.git로 처음부터 다시</p>
<hr>

<h3>12일차</h3>
<p>● 로그인 url 오류 고치기 ← 회원가입 / 로그인 폼의 무언가가 중복되어 발생한 것으로 불필요한 링크 없애서 해결</p>
<p>● 삭제하고 나서 기존 index페이지로 새로고침 되어야 하는 것 (~/delete로 주소 바뀌면 각종 잡 오류 발생했었기 때문) 해결 ← views.py의 stdisplay에는 delete_flag를 0으로 설정하고 stdelete와 stdelete2 함수에는 delete_flag를 1로 설정하고 그 값을 각각 index.html로 모두 보냄. 그리고 index.html의 자바스크립트에서 if({{delete_flag}} == 1){ window.location.href="{% url 'stdisplay' %}";}를 입력</p>
<p>● .env로 보안 시도해보기</p>
<hr>

<h3>13일차</h3>
<p>● .env 관련 작업 실패 → pw == "{{}}"가 아니라 pw == {{}}로 해결 → 그런데 서버에서 none 뜨면서 오류 발생</p>
<p>● os.environ.get 함수 디폴트값 넣으면 서버에서 none 안 뜨긴 하지만, 개발자도구에서 암호가 보임 → 개선 필요</p>
<hr>

<h3>14일차</h3>
<p>● 모든 코드 주석 작성</p>
<p>● 여전히 암호 보안 관련 해결해야 함</p>
<hr>

<h3>15일차</h3>
<p>● 암호 보안 문제를 models.py에 새로운 클래스모델(admin 암호 저장용) 추가하여 해결</p>
<p>● 이어서 views.py의 stdisplay에서 logout post되면 admin 암호(마지막 인덱스의 값)를 다른 값으로 바꿔서 로그아웃</p>
<p>● views.py의 stregister에서 암호 받아와서 저장하고 마지막 인덱스를 다시 HTML로 내보내서 마무리 </p>
<p>● DateTimeField를 입맛에 맞게 필터 적용 ← time 뒤에 |date:'Y-m-d H:i' 입력</p>
<hr>

<h4>16일차</h4>
<p>● 주석 추가, README 작성</p>
<p>● 마무리</p>
<hr>
