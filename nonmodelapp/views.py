from django.shortcuts import render
from django.http import HttpResponse

### DB 처리를 위한 사용자 라이브러리
from nonmodelapp.model_db_class.member import member as mem
from nonmodelapp.model_db_class.cart import cart
from nonmodelapp.model_db_class.lprod import lprod
from nonmodelapp.model_db_class.join import join

### 이메일 처리를 위한 사용자 라이브러리
from nonmodelapp.email_util import email_util

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

def setCartInsert(request):
    return HttpResponse()


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

####### 주문(장바구니) 정보 관리 #######
def getCartList(request):
    ### ORM 방식
    # cart_list = Cart.objects.all().order_by("-cart_no")

    ### NonModel
    # - cart.py에서 만들어준 함수를 이용해서 cart 테이블에서 cart_list 정보를 추출
    cart_list = cart.getCartList()
    return render(request, 
                  "nonmodelapp/cart/cart_list.html",
                  {"cart_list" : cart_list}) # <-- 모델에서 받은값

### 주문(장바구니) 상세정보 조회(1건 조회)
def getCartView(request):
    try:
    
        cart_no = request.GET.get("cart_no", "ERROR")
        cart_prod = request.GET.get("cart_prod", "ERROR")

        ### ORM
        # cart_view = Cart.objects.get(cart_no = cart_no,
                                #    cart_prod = cart_prod)
        ### NonModel
        cart_view = cart.getCart(cart_no, cart_prod)
    except:
        msg = '''
           <script type="text/javascript">
                alert('잘못된 접근입니다')
                location.href = '/nonmodel/cart_list/';
           </script> 
        '''
        return HttpResponse(msg)

    return render(request,
                "nonmodelapp/cart/cart_view.html",
                {"cart_no" : cart_no,
                "cart_prod" : cart_prod,
                "cart_view" : cart_view})

### 주문(장바구니) 수정 폼 페이지
def getCartUpdateForm(request):
    try:
        cart_no = request.GET.get("cart_no", "ERROR")
        cart_prod = request.GET.get("cart_prod", "ERROR")

        cart_view = cart.getCart(cart_no, cart_prod) 

    except:
        msg = '''
           <script type="text/javascript">
                alert('잘못된 접근입니다')
                location.href = '/nonmodel/cart_list/';
           </script> 
        '''
        return HttpResponse(msg)
 
    return render(request,
                    "nonmodelapp/cart/cart_update_form.html",
                    {"cart_no" : cart_no,
                    "cart_prod" : cart_prod,
                    "cart_view"  : cart_view})
    
### 주문(장바구니) 수정 처리하기
def getCartUpdate(request):
    try:
        
        cart_no = request.POST.get("cart_no", "Error")
        cart_prod = request.POST.get("cart_prod", "Error")
        cart_qty = request.POST.get("cart_qty", "Error")
        
       
        # Cart.objects.filter(cart_no=cart_no,
        #                     cart_prod=cart_prod).update(cart_qty=cart_qty)
        
        msg = """
                <script type='text/javascript'>
                    alert('수정됐다 임마');
                    location.href = '/nonmodel/cart_view/?cart_no={}&cart_prod={}';
                </script>
        """.format(cart_no, cart_prod)
        
        rs_chk = cart.setCartUpdate(cart_no, cart_prod, cart_qty)

    except:
        msg = '''
           <script type="text/javascript">
                alert('잘못된 접근입니다')
                location.href = '/nonmodel/cart_list/';
           </script> 
        '''
        return HttpResponse(msg)
    
    return HttpResponse(msg)

### 주문(장바구니) 정보 저장 폼 화면 처리
def getCartInsertForm(request) :
    return render(request,
                  "nonmodelapp/cart/cart_insert_form.html",
                  {})

### 주문(장바구니) 정보 저장 처리하기
def getCartInsert(request):
    try:
        if request.method == "POST":
            cart_member = request.POST.get("cart_member","error")
            cart_prod   = request.POST.get("cart_prod","error")
            cart_qty    = request.POST.get("cart_qty","error")
            cart_no     = request.POST.get("cart_no","error")

        elif request.method == "GET":
            cart_member = request.GET.get("cart_member","error")
            cart_prod   = request.GET.get("cart_prod","error")
            cart_qty    = request.GET.get("cart_qty","error")
            cart_no     = request.GET.get("cart_no","error")

        ### nonmodel
        rs_chk = cart.setCartInsert(cart_no, cart_prod, cart_qty, cart_member)

        msg = '''
                <script type='text/javascript'>
                    alert('정상적으로 저장되었습니다.')
                    location.href = '/nonmodel/cart_list/';
                </script>
        '''
    except:
        msg = '''
           <script type="text/javascript">
                alert('잘못된 접근입니다')
                location.href = '/nonmodel/mem_cart_list/';
           </script> 
        '''
        return HttpResponse(msg)
    # 4번 처리 : 
    return HttpResponse(msg)

    
### 주문(장바구니) 정보 삭제하기
def getCartDelete(request):
    try:
        cart_no = request.GET["cart_no"]
        cart_prod = request.GET["cart_prod"]
       
        msg = """
                <script type='text/javascript'>
                    alert('정상삭제');
                    location.href = '/nonmodel/cart_list/';
                </script>
        """
        ### NonModel
        cart.setCartDelete(cart_no,cart_prod)
                      # 
    except:
        msg = '''
           <script type="text/javascript">
                alert('잘못된 접근입니다')
                location.href = '/nonmodel/cart_list/';
           </script> 
        '''
        return HttpResponse(msg)
    return HttpResponse(msg)

###### 상품분류 검색에 의한 상품상세조회
def getSearchProd(request):
    lprod_gu = request.GET.get("lprod_gu", "")
    prod_id = request.GET.get("prod_id", "")

    ### 상품분류 selectbox에 들어갈 내용 조회하기
    # lprod_selbox = lprod.getLprodList()
    lprod_selbox = join.getSelBox_Lprod()

    ### 상품 selectbox에 들어갈 내용 DB조회하기
    # - 최초에는 상품분류가 선택이 안되어 있기에
    # - 조회된 상품분류에서 첫번째 상품분류의 값을 이용해서
    #   상품을 조회해서 상품 selectbox의 값을 채웁니다.
    if lprod_gu == "": # 들어온 값이 없다면
        lprod_gu = lprod_selbox[0]["lprod_gu"]

    prod_selbox = join.getSelBox_Lprod_Prod(lprod_gu)

    ### 선택된 상품분류 및 선택된 상품에 대해서
    #   - 상품 상세내용 조회하기
    ### - 최초에는 상품이 선택되어 있지 않기에
    #     prod_selbox에서 조회된 결과 중에 첫번째 값을 이용
    if prod_id == "":
        prod_id = prod_selbox[0]["prod_id"]

    prod_view = join.getLprod_Prod_Buyer(lprod_gu,prod_id)

    return render(request,
                  "nonmodelapp/search_prod/search_prod.html",
                  {"lprod_selbox": lprod_selbox,
                   "prod_selbox" : prod_selbox,
                   "prod_view" : prod_view,
                   "lprod_gu" : lprod_gu,
                   "prod_id" : prod_id})

############## [메일 발송 처리] ##############
### 메일 발송을 위한 폼 화면 처리
def getEmailForm(request) :
    return render(request,
                  "nonmodelapp/email_form/email_form.html",
                  {})

### 메일 발송 처리하기
def emailSend(request) : 
    emails = request.POST.get("emails", "")
    title = request.POST.get("title", "")
    content = request.POST.get("content", "")
    
    ### 여러건의 이메일 주소가 있는 경우까지 처리
    # - 리스트 타입으로 생성
    emails_list = emails.replace(" ","").split(",")

    ### 이메일 전송시키기 : email_util 사용
    send_chk = email_util.sendEmail(emails, title, content)

    ### 이메일 성공여부에 따른 페이지 전환 처리(script)
    # - 성공
    if send_chk > 0 :
        msg = """
            <script type="text/javascript">
                alert('성공적으로 메일이 발송되었습니다.!');
                location.href = 'nonmodel/';
            </script>
        """
    # - 실패
    else : 
        msg = """
            <script type="text/javascript">
                alert('메일 발송이 실패하였습니다.!');
                history.go(-1);
            </script>
        """
    return HttpResponse(msg)


