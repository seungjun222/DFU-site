import django.forms.fields
from django.shortcuts import render
from crud.models import crudstudent, zebal, miribogi, AdminPassword, UserPassword, CountChangeAP, RealAdminPassword
from django.contrib import messages
from crud.forms import stform

import os

def stdisplay(request):
    delete_flag = 0

    result=crudstudent.objects.all()

    m_haha = crudstudent.objects.values()
    m_haha = list(m_haha) # QuerySet인 m_haha를 리스트의 형태로 변환
    m_lst = [] # 곧 만들 이중리스트의 내부리스트에 해당
    m_lst2 = [] # 곧 만들 이중리스트에 해당
    for i in m_haha: # models.py에 있는 crudstudent db의 object들의 value 값들을 하나씩 돌며 반복
        for j in i.values(): # value 값들의 value 값들을 하나씩 돌며 반복하여 내부리스트에 저장
            m_lst.append(j)
        m_lst2.append(m_lst) # 내부리스트에 저장된 값들을 이중리스트에 저장
        m_lst = [] # 그 다움 내부리스트에 새로운 값들을 저장하기 위해 초기화

    m_savest2 = miribogi()
    m_result2 = miribogi.objects.all()

    """
        1. 이하 코드는 프론트단에서 체크하고 "대기하기" 누를 경우, 해당 데이터의 value값들을 미리보기 클래스모델에 저장하기 위한 알고리즘임
        2. 우선, HTML(index.html)에서 input 태그의 value를 {{displayst.id}}로 설정했으므로
        3. 여기서 int(request.POST.get("check"))를 통해 체크하여 대기하기된 데이터의 id를 불러와 m_umhaha에 저장
        4. 이후 반복문을 통해 이중리스트인 m_lst2의 길이만큼 돌고, if문을 통해 check된 id값을 찾을 경우에
        5. 또 다른 반복문을 통해 해당 id가 있는 데이터의 10가지 value 값들을 m_nebonegi 빈 리스트에 저장
        6. 이렇게 저장한 m_nebonegi 리스트를, 미리보기 클래스모델인 m_savest2의 10가지 value에 각각 저장
    """
    m_nebonegi = []
    if request.method == "POST":
        if request.POST.get("check"):
            m_umhaha = int(request.POST.get("check"))

            for i in range(0, len(m_lst2)):
                if m_umhaha == m_lst2[i][0]:
                    for j in range(0, 10):
                        m_nebonegi.append(m_lst2[i][j])

            m_savest2.id3 = m_nebonegi[0]
            m_savest2.time3 = m_nebonegi[1]
            m_savest2.name_ko3 = m_nebonegi[2]
            m_savest2.name_en3 = m_nebonegi[3]
            m_savest2.service3 = m_nebonegi[4]
            m_savest2.product3 = m_nebonegi[5]
            m_savest2.device3 = m_nebonegi[6]
            m_savest2.uploadedFile3 = m_nebonegi[7]
            m_savest2.crc3 = m_nebonegi[8]
            m_savest2.imageFile3 = m_nebonegi[9]

            m_savest2.save()

    """
        1. 이하 코드는 HTML에서 미리보기 모달창 가장 아래인 "대기"에 해당하는 데이터를 구성하기 위한 코드임
        2. 우선, m_result2는 이렇게 저장한 m_savest2(미리보기 클래스모델)을 object.all()한 것임 
        3. 이후 반복문과 조건문을 통해 m_result의 가장 마지막 인덱스를 zz라는 새로운 변수에 저장
        4. 이렇게 해서, 나중에 zz의 value값들을 HTML 상에서 띄울 수 있는 여건을 마련
    """
    zz=0

    for i in range(0, len(m_result2)):

        if i == len(m_result2) - 1:
            zz = m_result2[i]

   # ===================================================================================================================================

    """
        이하 코드는 미리보기 클래스모델에 저장한 데이터를 HTML 상에서 최종화면에 해당하는 zebal 클래스모델에 저장하기 위한 코드임
    """
    haha = crudstudent.objects.values()
    haha = list(haha) # QuerySet인 haha를 리스트의 형태로 변환
    lst = [] # 곧 만들 이중리스트의 내부리스트에 해당
    lst2 = [] # 곧 만들 이중리스트에 해당
    for i in haha: # models.py에 있는 crudstudent db의 object들의 value 값들을 하나씩 돌며 반복
        for j in i.values(): # value 값들의 value 값들을 하나씩 돌며 반복하여 내부리스트에 저장
            lst.append(j)
        lst2.append(lst) # 내부리스트에 저장된 값들을 이중리스트에 저장
        lst = [] # 그 다움 내부리스트에 새로운 값들을 저장하기 위해 초기화

    savest2=zebal()
    result2=zebal.objects.all()

    if request.method=="POST":
        if request.POST.get("nebonegi_button"):

            # miribogi 클래스의 마지막 인덱스의 value값들을 zebal 클래스에 저장해야함
            for i in range(0, len(m_result2)):
                if i == len(m_result2) - 1:
                    zz = m_result2[i]

            savest2.id2 = zz.id3
            savest2.time2 = zz.time3
            savest2.name_ko2 = zz.name_ko3
            savest2.name_en2 = zz.name_en3
            savest2.service2 = zz.service3
            savest2.product2 = zz.product3
            savest2.device2 = zz.device3
            savest2.uploadedFile2 = zz.uploadedFile3
            savest2.crc2 = zz.crc3
            savest2.imageFile2 = zz.imageFile3
            savest2.save()

    """
        1. 보안을 위해 '닷엔브'와 'os.environ.get'메소드를 사용하였지만, 서버상에서 정상 작동안함
        2. 따라서 콤마 뒤에 값을 Default 값으로 일단 설정했으나 이 역시 제 3자가 개발자도구로 볼 수 있음
        3. 이에 대해서 추후에 해결이 필요함
    """
    # EDIT_P = os.environ.get('EDIT_PASSWORD', '1234')
    # DELETE_P = os.environ.get('DELETE_PASSWORD', '1234')
    # EXPORT_P = os.environ.get('EXPORT_PASSWORD', '1234')

    """
        1. 사용자가 Admin 로그아웃을 할 때마다 count하는 클래스모델에서 1씩 추가하여 로그인/로그아웃 여부 판별
        2. 사용자가 Admin 암호변경을 할 때마다 그 변경한 암호를, 정답 Admin 암호 클래스모델의 value값에 저장
    """
    cc_ap = CountChangeAP()
    r_ap = RealAdminPassword()

    if request.method == "POST":
        if request.POST.get("logout"):
            cc_ap.cnt += 1
            cc_ap.save()

        if request.POST.get("change_submit"):
            change_p = request.POST.get("nebonegi_button2")
            print("change_p:{}".format(change_p))
            r_ap.realpassword = change_p
            r_ap.save()

    """
        1. 유저가 입력한 사용자 암호를 index.html에서 버튼암호 입력하는 데에 재사용하기 위해 아래와 같은 코드 작성
    """

    upShow = UserPassword.objects.values()
    upShow = list(upShow)  # QuerySet인 upShow를 리스트의 형태로 변환

    up_lst = []  # 곧 만들 리스트에 해당
    for i in upShow:  # models.py에 있는 UserPassword db의 object들의 value 값들을 하나씩 돌며 반복
        for j in i.values():  # value 값들의 value 값들을 하나씩 돌며 반복하여 리스트에 저장
            up_lst.append(j)
    print(up_lst) # [1, 'qewr1324']

    if len(up_lst) >= 1:
        up = up_lst[-1] # 리스트에 계속 append 되는구조라서 인덱스를 '-1'로 설정했음. 그런데 append하기전에 delete해서 충분히 로직 잘 짤 수 있을 듯. 그런데 일단 계속 append하는 구조로만 진행.
    else:
        up = 0 # 값 초기화

    return render(request,"index.html",{"crudstudent":result, "zebal":result2, "z":zz, "m_result2":m_result2, "delete_flag":delete_flag, "up":up})

def stinsert(request):
    if request.method=="POST":
        if request.POST.get('name_ko') and request.POST.get('name_en') and request.POST.get('service') and request.POST.get('product') and request.POST.get('device') and request.FILES.get('uploadedFile') and request.POST.get('crc') and request.FILES.get('imageFile'):
            savest=crudstudent()
            savest.name_ko=request.POST.get('name_ko')
            savest.name_en=request.POST.get('name_en')
            savest.service=request.POST.get('service')
            savest.product=request.POST.get('product')
            savest.device=request.POST.get('device')
            savest.uploadedFile=request.FILES.get('uploadedFile')
            savest.crc=request.POST.get('crc')
            savest.imageFile=request.FILES.get('imageFile')
            savest.save()
            messages.success(request, "정상적으로 " + savest.name_ko + "의 등록이 완료되었습니다!")
            return render(request,"create.html")

    return render(request,"create.html")

def stfinal(request):
    result2=zebal.objects.all()
    return render(request,"final.html",{"zebal":result2})

def stedit(request,id):
    getstudentdetails= crudstudent.objects.get(id=id)
    return render(request,'edit.html',{"crudstudent":getstudentdetails})

def stupdate(request,id):
    stupdate=crudstudent.objects.get(id=id)
    form=stform(request.POST,instance=stupdate)
    if form.is_valid():
        form.save()
        messages.success(request,"수정이 정상적으로 완료되었습니다!")
        return render(request,"edit.html",{"crudstudent":stupdate})

def stdelete(request,id):
    deletestudent = crudstudent.objects.get(id=id)
    deletestudent.delete()
    result=crudstudent.objects.all()

    delete_flag = 1

    return render(request,"index.html",{"crudstudent":result, "delete_flag":delete_flag})

def stdelete2(request,id):
    deletestudent2 = zebal.objects.get(id=id)
    deletestudent2.delete()
    result2 = zebal.objects.all()

    delete_flag = 1

    return render(request,"index.html",{"zebal":result2, "delete_flag":delete_flag})

# =====================================================================================================================

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def register(request):
    form = UserCreationForm
    user_flag = 0 # 회원가입 폼 제출 못할 경우, 추후 HTML(register.html) 상에서 Admin 암호 prompt 창을 계속 띄우기 위해 user_flag 설정

    cc_ap = CountChangeAP()
    if cc_ap.cnt % 2 == 1:
        print("Admin 로그아웃")
        IsAdminOut = 1
    elif cc_ap.cnt % 2 == 0:
        print("Admin 로그인")
        IsAdminOut = 0

    if request.method == 'POST':
        regForm=UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            """
                regForm.cleaned_data 하면 결과가 아래와 같이 나옴 (실제 입력한 ID와 PW)
                {'username': 'seungjun444', 'password1': 'qewr1324', 'password2': 'qewr1324'}
            """
            password1 = regForm.cleaned_data['password1']

            up = UserPassword()
            """
                 ★★★ 사용자가 장고에서 제공하는 회원가입 양식에서 입력한 암호를 models.py의 UserPassword 클래스모델에 저장
            """
            up.password1 = password1
            up.save()

            messages.success(request, '회원가입이 정상적으로 완료되었습니다!.')
            user_flag = 1 # 회원가입 폼 제출 성공하여, user_flag가 1이 됨에따라, 추후 HTML(register.html)에서 암호 prompt 자동생성 방지

        """
            1. models.py에서 AdminPassword 새로운 클래스모델 생성
            2. 오직 admin 비밀번호를 저장하기 위한 데이터베이스
            3. 사용자가 admin 비밀번호를 입력하면 받아와서 모두 저장함
        """

        if request.POST.get('password'):
            ap = AdminPassword()
            ap.password = request.POST.get('password')
            ap.save()

    """
        1. 사용자가 admin 비밀번호를 정확히 입력했는지를 판단하기 위해 마지막 인덱스만을 추출
        2. 추출한 마지막 인덱스를 apLast라는 변수에 저장하여 HTML(register.html)에 보냄
        3. 추후 HTML(register.html)에서 장고 템플릿 문법 중 조건문을 통해, 비밀번호 정답 여부를 판별
    """

    apShow = AdminPassword.objects.all()

    apLast = 0 # apLast 값 초기화 선언 (이거 안하면 오류남)
    for i in range(0, len(apShow)):
        if i == len(apShow) - 1:
            apLast = apShow[i]

    """
        1. 정답 Admin 암호를 저장하기 위해 클래스모델 생성
        2. 리스트로 타입변경 후 마지막 인덱스 값을 core(정답 Admin 암호)로 설정
        3. 사용자가 Admin 암호 변경할 때마다 리스트의 길이가 1씩 늘어날 것이므로 마지막 인덱스 값을 주목한 것임
    """

    r_apShow = RealAdminPassword.objects.values()
    r_apShow = list(r_apShow)
    r_ap_list = []  # 곧 만들 리스트에 해당
    for i in r_apShow:  # models.py에 있는 UserPassword db의 object들의 value 값들을 하나씩 돌며 반복
        for j in i.values():  # value 값들의 value 값들을 하나씩 돌며 반복하여 리스트에 저장
            r_ap_list.append(j)

    if len(r_ap_list) >= 1:
        core = str(r_ap_list[-1]) # 리스트에 계속 append 되는구조라서 인덱스를 '-1'로 설정했음. 그런데 append하기전에 delete해서 충분히 로직 잘 짤 수 있을 듯. 그런데 일단 계속 append하는 구조로만 진행.
    else:
        core = '0' # 값 초기화

    return render(request, 'register.html',{'form':form, 'user_flag':user_flag, 'apLast':apLast, 'core':core, 'IsAdminOut':IsAdminOut})

def stlogin(request):
    return render(request, './registration/login.html')

# =====================================================================================================================
    # def stdisplay에 썼었던 코드

    # nebonegi = [] # 아까 만들었던 (기존에 존재하는 QuerySet을 리스트로 변환했던) lst2에서 선택한 개체들을 저장 및 불러오기 위한 빈 리스트 생성
    # if request.method=="POST": # 프론트엔드 단에서 "내보내기" 버튼을 submit하여 post될 경우
    #     if request.POST.get("check"): # 해당 post가 checkbox의 name인 check와 일치할 경우
    #         umhaha = int(request.POST.get("check")) # checkbox의 value값인 {{displayst.id}}를 받아옴. str이라 int로 변환
    #         print("umhaha:{}".format(umhaha))
    #         for i in range(0, len(lst2)): # 이중리스트의 전체 길이만큼 반복
    #             if umhaha == lst2[i][0]: # 선택한 checkbox의 value값인 {{displayst.id}}와 이중리스트의[i][0](즉, 각 내부리스트의 id)가 일치할 경우 => (체크박스에서 선택한 해당 데이터들만 불러오기 위해)
    #                 for j in range(0, 10): # 0부터 9번 인덱스까지 (models.py의 변수들이 10개이므로)
    #                     nebonegi.append(lst2[i][j]) # (아까 만든 빈 리스트에 선택한 데이터의 모든 값들을 append)
    #         print("성공:{}".format(nebonegi))
    #         savest2.id2 = nebonegi[0] # 영구적으로 저장하기 위해 선택한 데이터의 모든 값들을 append한 리스트의 인덱스별로 models.py의 db에 저장
    #         savest2.time2 = nebonegi[1] # 이하 동일
    #         savest2.name_ko2 = nebonegi[2]
    #         savest2.name_en2 = nebonegi[3]
    #         savest2.service2 = nebonegi[4]
    #         savest2.product2 = nebonegi[5]
    #         savest2.device2 = nebonegi[6]
    #         savest2.uploadedFile2 = nebonegi[7]
    #         savest2.crc2 = nebonegi[8]
    #         savest2.imageFile2 = nebonegi[9]
    #
    #         savest2.save()