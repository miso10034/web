from django.shortcuts import render
from django.http import HttpResponse

from thirdapp.model_db_class.cart import cart
from thirdapp.model_db_class.join import join

def index(request):
    return render(request,
                  "thirdapp/index.html",{})

### 주문장바구니 정보 관리
def getCartList(request):
    cart_list = cart.getCartList()
    return render(request,
                  "thirdapp/cart/cart_list.html",
                  {"cart_list" : cart_list})

### 주문(장바구니) 상세정보 조회
def getCartView(request):
    cart_no = request.GET.get("cart_no","error")
    cart_prod = request.GET.get("cart_prod","error")

    cart_view = cart.getCart(cart_no, cart_prod)
    return render(request,
                  "thirdapp/cart/cart_view.html",
                  {"cart_no": cart_no,
                   "cart_prod": cart_prod,
                   "cart_view": cart_view})

def getCartUpdateForm(request):
    cart_no = request.GET.get("cart_no","error")
    cart_prod = request.GET.get("cart_prod","error")

    cart_view = cart.getCart(cart_no, cart_prod)

    return render(request,
                  "thirdapp/cart/cart_update_form.html",
                  {"cart_no" : cart_no,
                   "cart_prod" : cart_prod,
                   "cart_view":cart_view})

def getCartUpdate(request):
    cart_no = request.POST.get("cart_no","error")
    cart_prod = request.POST.get("cart_prod","error")
    cart_qty = request.POST.get("cart_qty","error")

    rs_chk = cart.setCartUpdate(cart_no,cart_prod,cart_qty)
    msg = """
            <script type='text/javascript'>
                alert("수정됐다");
                location.href = '/third/cart_view/?cart_no={}&cart_prod={}';
                </script>
        """.format(cart_no,cart_prod)
    return HttpResponse(msg)

### 주문(장바구니) 정보 저장 폼 화면 처리
def getCartInsertForm(request) :
    return render(request,
                  "thirdapp/cart/cart_insert_form.html",
                  {})

### 주문장바구니 정보 저장 처리하기
def getCartInsert(request):
    if request.method == "POST":
        cart_member = request.POST.get("cart_member","error")
        cart_prod = request.POST.get("cart_prod", "error")
        cart_qty = request.POST.get("cart_qty","error")
        cart_no = request.POST.get("cart_no","error")
    
    elif request.method == "GET":
        cart_member = request.GET.get("cart_member","error")
        cart_prod = request.GET.get("cart_prod", "error")
        cart_qty = request.GET.get("cart_qty","error")
        cart_no = request.GET.get("cart_no","error")

    rs_chk = cart.setCartInsert(cart_no, cart_prod, cart_qty, cart_member)

    msg = '''
                <script type='text/javascript'>
                    alert('정상적으로 저장되었습니다.')
                    location.href = '/third/cart_list/';
                </script>
        '''
    return HttpResponse(msg)

### 주문(장바구니) 정보 삭제하기
def getCartDelete(request):
    try:
        cart_no = request.GET["cart_no"]
        cart_prod = request.GET["cart_prod"]
       
        msg = """
                <script type='text/javascript'>
                    alert('정상삭제');
                    location.href = '/third/cart_list/';
                </script>
        """
        ### NonModel
        cart.setCartDelete(cart_no,cart_prod)
                      # 
    except:
        msg = '''
           <script type="text/javascript">
                alert('잘못된 접근입니다')
                location.href = '/third/cart_list/';
           </script> 
        '''
        return HttpResponse(msg)
    return HttpResponse(msg)

###### 상품분류 검색에 의한 상품상세조회
def getSearchProd(request):
    lprod_gu = request.GET.get("lprod_gu", "")
    prod_id = request.GET.get("prod_id", "")

    lprod_selbox = join.getSelBox_Lprod()

    if lprod_gu == "": # 들어온 값이 없다면
        lprod_gu = lprod_selbox[0]["lprod_gu"]

    prod_selbox = join.getSelBox_Lprod_prod(lprod_gu)

    if prod_id == "":
        prod_id = prod_selbox[0]["prod_id"]

    prod_view = join.getLprod_Prod_Buyer(lprod_gu,prod_id)

    return render(request,
                  "thirdapp/search_prod/search_prod.html",
                  {"lprod_selbox": lprod_selbox,
                   "prod_selbox" : prod_selbox,
                   "prod_view" : prod_view,
                   "lprod_gu" : lprod_gu,
                   "prod_id" : prod_id})