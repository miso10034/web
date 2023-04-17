from django.shortcuts import render
from django.http import HttpResponse

from nonmodelapp.model_db.member import member as mem
from nonmodelapp.model_db.cart import cart 

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



####### 주문(장바구니) 정보 관리 #######
def getCartList(request):
    # cart_list = Cart.objects.all().order_by("-cart_no")
    cart_list = cart.getCartList()
    return render(request, 
                  "nonmodelapp/cart/cart_list.html",
                  {"cart_list" : cart_list}) 

### 주문(장바구니) 상세정보 조회(1건 조회)
def getCartView(request):
    try:
        cart_no = request.GET.get("cart_no", "ERROR")
        cart_prod = request.GET.get("cart_prod", "ERROR")

        cart_view = cart.getCartV(cart_no = cart_no,
                                    cart_prod = cart_prod)

    except:
        msg = '''
           <script type="text/javascript">
                alert('잘못된 접근입니다')
                location.href = '/nonmodel/cart_list/';
           </script> 
        '''
        return HttpResponse(msg)
    
    # 3번 처리 : cart_view.html 생성
    # 4번 처리
    return render(request,
                "nonmodelapp/cart/cart_view.html",
                {"cart_no" : cart_no,
                "cart_prod" : cart_prod,
                "cart_view" : cart_view})

### 주문(장바구니) 수정 폼 페이지
def setCartUpdateForm(request):
    try:
        cart_no = request.GET.get("cart_no", "ERROR")
        cart_prod = request.GET.get("cart_prod", "ERROR")

        # cart_view = Cart.objects.get(cart_no=cart_no,
        #                            cart_prod = cart_prod)
        cart_view = cart.getCartView(cart_no)
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
        cart_view = cart.setCartUpdate(cart_no,cart_prod,cart_qty)
    except:
        msg = '''
           <script type="text/javascript">
                alert('잘못된 접근입니다')
                location.href = '/oracle/cart_list/';
           </script> 
        '''
        return HttpResponse(msg)
    
    msg = """
            <script type='text/javascript'>
                alert('수정됐다 임마');
                location.href = '/nonmodel/cart_view/?cart_no={}&cart_prod={}';
            </script>
        """.format(cart_no, cart_prod)
        
    
    
    return HttpResponse(msg)
    

