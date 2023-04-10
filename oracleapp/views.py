from django.shortcuts import render
from django.http import HttpResponse
from .models import Member

### oracleapp의 index 페이지
def index(request):
    #return HttpResponse("Oracle index 페이지 입니다.")
    return render(request,
                  'oracleapp/index.html',
                  {})

######## [회원정보] #########
### 회원정보 전체 조회하기
def getMemberList(request):
    # 데이터베이스와 연결 
    ### 회원정보 전체 조회하기(O(objects)RM 방식)
    # Select * From member
    # Member라는 클래스에서 전체조회할거야
    # all() : 전체 조회 함수
    mem_list = Member.objects.all()
    return render(request,
                  'oracleapp/member/mem_list.html',
                  {"mem_list":mem_list})
