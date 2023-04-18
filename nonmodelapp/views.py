from django.shortcuts import render
from django.http import HttpResponse

from nonmodelapp.model_db_class.member import member as mem
# from nonmodelapp.model_db.cart import cart 

### 최초 nonmodel root 페이지
def index(request):
    return render(request,
                  "nonmodelapp/index.html",
                  {})

### 회원 전체조회 
def getMemberList(request):
    # mem_list = Member.objects.all()
    mem_list = mem.getMemberList()
    return render(request,
                    "nonmodelapp/member/mem_list.html",
                    {"mem_list": mem_list})

### 회원 상세조회 : 한건 조회
def getMemberView(request):
    try :
        mem_id = request.GET.get("mem_id", "a001")
        
        mem_view = mem.getMember(mem_id)

    except:
        msg = """
            <script type="text/javascript">
                alert('잘못된 접근!');
                location.href = '/nonmodel/mem_list/';
            </script>
        """
        return HttpResponse(msg)
    
    return render(request,
                "nonmodelapp/member/mem_view.html",
                {"mem_view": mem_view,
                "mem_id": mem_id})

### 회원 정보 수정 폼 페이지
def getMemUpdateForm(request):
    try:
        mem_id = request.GET.get("mem_id", "ERROR")
        
        # mem_view = Member.objects.get(mem_id = mem_id)
        mem_view = mem.getMember(mem_id)
    except:
        msg ="""
            <script type="text/javascript">
                alert("잘못접근")
                location.href="/nonmodel/mem_list/';
            </sciprt>
        """
        return HttpResponse(msg)

    return render(request,
                  "nonmodelapp/member/mem_update_form.html",
                  {"mem_id":mem_id,
                   "mem_view":mem_view})

### 회원정보 수정 폼 페이지
def getMemUpdate(request):
    try:
        mem_id = request.POST["mem_id"]
        mem_pass = request.POST["mem_pass"]
        mem_add1 = request.POST["mem_add1"]

        # Member.objects.filter(mem_id = mem_id).update(mem_pass = mem_pass,
        #                                           mem_add1 = mem_add1)
        rs_msg = mem.setMemberUpdate(mem_pass, mem_add1, mem_id)

    except:
        msg = '''
           <script type="text/javascript">
                alert('잘못된 접근입니다')
                location.href = '/nonmodel/mem_list/';
           </script> 
        '''
        return HttpResponse(msg)
  
    msg = """
            <script type = 'text/javascript'>
                alert('정상적으로 수정되었습니다!');
                location.href = '/nonmodel/mem_view/?mem_id={}';
            </script>
        """.format(mem_id)
        

    return HttpResponse(msg)



# ####### 주문(장바구니) 정보 관리 #######
# def getCartList(request):
#     # cart_list = Cart.objects.all().order_by("-cart_no")
#     cart_list = cart.getCartList()
#     return render(request, 
#                   "nonmodelapp/cart/cart_list.html",
#                   {"cart_list" : cart_list}) 

# ### 주문(장바구니) 상세정보 조회(1건 조회)
# def getCartView(request):
#     try:
#         cart_no = request.GET.get("cart_no", "ERROR")
#         cart_prod = request.GET.get("cart_prod", "ERROR")

#         cart_view = cart.getCartV(cart_no = cart_no,
#                                     cart_prod = cart_prod)

#     except:
#         msg = '''
#            <script type="text/javascript">
#                 alert('잘못된 접근입니다')
#                 location.href = '/nonmodel/cart_list/';
#            </script> 
#         '''
#         return HttpResponse(msg)
    
#     # 3번 처리 : cart_view.html 생성
#     # 4번 처리
#     return render(request,
#                 "nonmodelapp/cart/cart_view.html",
#                 {"cart_no" : cart_no,
#                 "cart_prod" : cart_prod,
#                 "cart_view" : cart_view})

# ### 주문(장바구니) 수정 폼 페이지
# def setCartUpdateForm(request):
#     try:
#         cart_no = request.GET.get("cart_no", "ERROR")
#         cart_prod = request.GET.get("cart_prod", "ERROR")

#         # cart_view = Cart.objects.get(cart_no=cart_no,
#         #                            cart_prod = cart_prod)
#         cart_view = cart.getCartView(cart_no)
#     except:
#         msg = '''
#            <script type="text/javascript">
#                 alert('잘못된 접근입니다')
#                 location.href = '/nonmodel/cart_list/';
#            </script> 
#         '''
#         return HttpResponse(msg)

#     return render(request,
#                     "nonmodelapp/cart/cart_update_form.html",
#                     {"cart_no" : cart_no,
#                     "cart_prod" : cart_prod,
#                     "cart_view"  : cart_view})
    
# ### 주문(장바구니) 수정 처리하기
# def getCartUpdate(request):
#     try:
#         cart_no = request.POST.get("cart_no", "Error")
#         cart_prod = request.POST.get("cart_prod", "Error")
#         cart_qty = request.POST.get("cart_qty", "Error")
        
#         # Cart.objects.filter(cart_no=cart_no,
#         #                     cart_prod=cart_prod).update(cart_qty=cart_qty)
#         cart_view = cart.setCartUpdate(cart_no,cart_prod,cart_qty)
#     except:
#         msg = '''
#            <script type="text/javascript">
#                 alert('잘못된 접근입니다')
#                 location.href = '/oracle/cart_list/';
#            </script> 
#         '''
#         return HttpResponse(msg)
    
#     msg = """
#             <script type='text/javascript'>
#                 alert('수정됐다 임마');
#                 location.href = '/nonmodel/cart_view/?cart_no={}&cart_prod={}';
#             </script>
#         """.format(cart_no, cart_prod)
        
    
    
#     return HttpResponse(msg)

### 로그인 화면 페이지 처리
def login_form(request):
    return render(request,
                  "nonmodelapp/login/login_form.html",
                  {})

### 로그인 인증 처리하기
def login_chk(request):
    mem_id = request.POST["mem_id"]
    mem_pass = request.POST["mem_pass"]

    mem_view = mem.getLoginChk(mem_id,mem_pass)
    # mem_id,mem_pass를 넘겨줘야 sql을 완성할 수 있음

    if mem_view.get("RS") == "Data_None" :
        msg ="""
            <script type="text/javascript">
                alert("아이디 또는 패스워드를 확인해주세요!");
                history.go(-1);
            </script>
        """
        return HttpResponse(msg)
    
    elif mem_view.get("RS") == "DB_ERROR" :
        msg ="""
            <script type="text/javascript">
                alert("시스템에 문제가 있네요! 잠시 후 다시 접근하세요!~!");
                location.href = '/'
            </script>
        """
        return HttpResponse(msg)
    
    ### 로그인 상태를 유지하기 위한 기능 : 세션(session) 처리
    # - request객체 내에 존재하는 session 변수를 사용해서
    # - 서버 영역에 값을 저장해 놓는 기능
    # - 사용자가 로그아웃 또는 브라우저를 종료하면 서버와의 접속이 끊어지고,
    # - 이때, request 객체 내에 있는 session 변수내에 key들은 삭제 됩니다.

    # - session변수는 딕셔너리 타입의 변수로 Key값과 Value값을 넣어주면됨
    # - request 객체는 html페이지 어디에서든 사용가능하기에
    # - session변수도 views 및 html 어디서든지 사용 가능
    #   (request 객체를 사용할 수 있는 모든 곳..)

    request.session["ses_mem_id"] = mem_id
    request.session["ses_mem_name"] = mem_view.get("mem_name")
    
    msg ="""
        <script type="text/javascript">
            alert("환영!-! [{}]님 로그인 됐다!");
            location.href = '/'
        </script>
    """.format(mem_view.get("mem_name"))
    # 위는 html영역이어서 location.href = '위치' -> url 패턴을 써줌
    
    
    return HttpResponse(msg)

### 로그아웃 처리 기능 
def logout_chk(request):
    ### 로그아웃의 의미 : session 정보를 삭제하면 됨...
    request.session.flush()
    msg = """
        <script type="text/javascript">
            alert('로그아웃 되었습니다.');
            location.href = '/';
        </script>
    """
    return HttpResponse(msg)