from django.shortcuts import render
from django.http import HttpResponse

from .models import Member

### oracleapp의 index 페이지
def index(request) :
    return render(request,
                  "oracleapp/index.html",
                  {})
    # return HttpResponse("Oracle 페이지 입니다.")

######### [회원정보] ########
### 회원정보 전체 조회하기
def getMemberList(request) :
    # 데이터베이스와 연결 
    ### 회원정보 전체 조회하기(O(objects)RM 방식)
    # Select * From member
    # Member라는 클래스에서 전체조회할거야
    # all() : 전체 조회 함수
    mem_list = Member.objects.all()
    return render(request,
                  "oracleapp/member/mem_list.html",
                  {"mem_list" : mem_list})


### 회원정보 상세 조회하기
def getMemberView(request) :

    # <문제>mem_view.html 페이지로 이동
    # getMemberView() 함수 사용
    # 클릭했을 때의 회원 정보를 getMemberview() 함수에 넘어가야함
    #  패턴 : mem_view

    ### 변수 mem_id로 전달받기
    # - 전달 받은 후 mem_id 출력하기
    # get 방식
    # mem_id = request.GET["mem_id"] -> 딕셔너리에서 뽑아내는 방식 값이 없으면 오류가 난다.
    # get-> 함수 / 함수 이용시 값이 없으면 공백 / 값이 없으면 ERROR로 대체하겠다.
    mem_id = request.GET.get("mem_id", "ERROR")

    # primarykey인 mem_id로 조회시 pk가 mem_id인 값을 조회한다는 뜻
    ### 회원정보 상세(한건) 조회하기(ORM 방식)
    """
        Select * 
        From member
        Where mem_id = mem_id
    """
    ### 모델(M) 처리하기 (한건 조회 : get() 사용)
    # - get(Member.mem_id = 전송받은 mem_id)
    mem_view = Member.objects.get(mem_id = mem_id)
    # {"mem_id" : "아이디", "mem_pass":"패스워드",
    #  "mem_name":"이름", "mem_add1":"주소1"}
    # return HttpResponse()
    return render(request,
                  "oracleapp/member/mem_view.html",
                  {"mem_view" : mem_view,
                   "mem_id" : mem_id})

### 회원정보 수정 폼 페이지
def getMemUpdateForm(request) :
    # 1. 전송데이터가 있으면 받기(get or post)
    # 2. DB 입력/수정/삭제/조회 시 models.py 처리
    # 3. DB처리 결과가 있으면 html에 넘겨주기
    
    mem_id = request.GET.get("mem_id", "ERROR")

    # {"mem_id" : "아이디", "mem_pass":"패스워드",
    #  "mem_name":"이름", "mem_add1":"주소1"}
    mem_view = Member.objects.get(mem_id = mem_id)

    return render(request,
                  "oracleapp/member/mem_update_form.html",
                  {"mem_id" : mem_id,
                   "mem_view" : mem_view}) 
