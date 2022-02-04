from django.shortcuts import render
from crud.models import crudstudent, zebal, miribogi
from django.contrib import messages
from crud.forms import stform

def stdisplay(request):
    result=crudstudent.objects.all()


    m_haha = crudstudent.objects.values()
    m_haha = list(m_haha)
    m_lst = []
    m_lst2 = []
    for i in m_haha:
        for j in i.values():
            m_lst.append(j)
        m_lst2.append(m_lst)
        m_lst = []

    m_savest2 = miribogi()
    m_result2 = miribogi.objects.all()

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

    zz=0

    for i in range(0, len(m_result2)):

        if i == len(m_result2) - 1:
            zz = m_result2[i]

   # ===================================================================================================================================

    haha = crudstudent.objects.values()
    haha = list(haha) # QuerySet을 리스트로 변환
    lst = [] # 곧 만들 이중리스트의 내부 리스트에 해당
    lst2 = [] # 곧 만들 이중리스트에 해당
    for i in haha: # models.py에 있는 crudstudent db의 object들의 value 값들을 하나씩 돌며 반복
        for j in i.values(): # value 값들의 value값들을 하나씩 돌며 반복하여 내부리스트에 저장
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

    # ===================================================================================================================================

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

    return render(request,"index.html",{"crudstudent":result, "zebal":result2, "z":zz, "m_result2":m_result2})

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
            messages.success(request,"The Record "+savest.name_ko+" is saved successfully !")
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
        messages.success(request,"The Student Record Updated Successfull")
        return render(request,"edit.html",{"crudstudent":stupdate})

def stdelete(request,id):
    deletestudent = crudstudent.objects.get(id=id)
    deletestudent.delete()
    result=crudstudent.objects.all()

    # stdisplay처럼 index.html로 render하기 때문에 stdisplay가 넘긴 값들을 동일하게 넘겨주어야함

    m_result2 = miribogi.objects.all()
    result2 = zebal.objects.all()
    zz = 0
    for i in range(0, len(m_result2)):
        if i == len(m_result2) - 1:
            zz = m_result2[i]

    return render(request,"index.html",{"crudstudent":result, "zebal":result2, "z":zz, "m_result2":m_result2})

def stdelete2(request,id):
    deletestudent2 = zebal.objects.get(id=id)
    deletestudent2.delete()
    result2 = zebal.objects.all()

    # stdisplay처럼 index.html로 render하기 때문에 stdisplay가 넘긴 값들을 동일하게 넘겨주어야함

    result=crudstudent.objects.all()

    m_result2 = miribogi.objects.all()
    zz = 0
    for i in range(0, len(m_result2)):
        if i == len(m_result2) - 1:
            zz = m_result2[i]

    return render(request,"index.html",{"crudstudent":result, "zebal":result2, "z":zz, "m_result2":m_result2})

# =====================================================================================================================

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def register(request):
    form = UserCreationForm
    if request.method == 'POST':
        regForm=UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            messages.success(request, 'User has been registered.')
    return render(request, 'register.html',{'form':form})

def stlogin(request):
    return render(request, './registration/login.html')

# =====================================================================================================================
