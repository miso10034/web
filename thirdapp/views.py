from django.shortcuts import render
from django.http import HttpResponse

from thirdapp.model_db_class.cart import cart
from thirdapp.model_db_class.join import join
from thirdapp.model_db_class.member import member as mem
from thirdapp.file_util.file_util import File_Util
## 페이징 처리를 위한 라이브러리
from django.core.paginator import Paginator

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

## 페이징 처리하기 ##
# - 페이지 처리를 위해서는 paginator 라이브러리 필요함
# - 회원정보 전체리스트 목록을 샘플로 진행
def getMemberListPaging(request):
    
    # 현재 페이지 번호 받기
    now_page = request.GET.get("page","1")
    now_page = int(now_page)
    mem_list = mem.getMemberList()

    # 한 화면에 10개 행씩 추출
    # 화면에 보여줄 행의 갯수 정의 10개씩 보여주기
    num_row = 10
    p = Paginator(mem_list,num_row)
    rows_data = p.page(now_page)
    # 시작 페이지 번호 계산
    start_page = (now_page-1) // num_row * num_row + 1
    # 종료 페이지 번호 계산
    end_page = start_page + 9
    # 종료 페이지 번호가 종료 행의 갯수 보다 크면
    if end_page > p.num_pages:
        end_page = p.num_pages

    is_prev = False
    is_next = False

    if start_page > 1:
        is_prev = True
    if end_page < p.num_pages:
        is_next = True
    context = {
        "cart_list":rows_data,
        "page_range" : range(start_page, end_page+1),
        "is_prev" : is_prev,
        "is_next" : is_next,
        "start_page" : start_page,
        "now_page" : now_page
    }
    return render(request,
                  "thirdapp/paging/mem_list.html",
                  context)


######### File Upload / Download 처리하기 #########
### file_util.py 라이브러리의 클래스 import 하기
### 파일 업로드를 위한 폼 페이지
def getFileInsertForm(request):
    return render(request,
                  "thirdapp/file_UpDown/file_insert_form.html",
                  {})

### File Upload 처리하기
def setFileInsert(request):
    try:
        title = request.POST.get("title")

        if request.FILES.get("file_nm") is not None :
            file_nm = request.FILES.get("file_nm")
        else : 
            file_nm = ""
    except:
        pass

    if file_nm != "":

        ###############[ File Upload 처리하기 ]###############
        ### - 파일 업로드 폴더 위치 지정(루트경로) 및 물리적 위치 생성하기 
        upload_dir = "./thirdapp/static/nonmodelapp/file_UpDown/"
        download_dir = "./thirdapp/static/nonmodelapp/file_UpDown/"
        
        ### 파일을 페이지에 보여줄 경우 : 폴더 전체 경로 지정
        img_dir = "/static/thirdapp/file_UpDown/"

        ### File_Util 클래스 생성하기
        fu = File_Util()

        ### 초깃값 셋팅(설정)하기
        fu.setUpload(file_nm, upload_dir, img_dir, download_dir)

        ### 파일 업로드 실제 수행하기
        fu.fileUpload()

        ### Table에 데이터 저장
        # fu.goDataSave(no, title, img_full_name, download_full_name)

        ################ [업로드된 파일 정보 조회] ##################
        ### 파일 사이즈
        file_size = fu.file_size
        ### 업로드된 파일명
        filename = fu.file_nm
        ### <img> 태그에 넣을 src 전체 경로
        img_full_name = fu.img_full_name
        ### (DB 저장용) 다운로드 전체경로+파일명
        download_full_name = fu.download_full_name
    
        ####### [Database 이용시]
        # 컬럼은 두개사용 : img_full_name, download_full_name


    msg = """
        <p>img_full_name : {0}</p>
        <p>file_size : {1}</p>
        <p>filename : {2}</p>
        <p>다운로드 파일명 :
            <a href='/third/file_down/?download_full_name={3}'>{2}</a>
        </p>
        <p><img src='{0}'></p>
    """.format(img_full_name, file_size,
               filename, download_full_name)

    return HttpResponse(msg)

### File Download 처리하기
def setFileDown(request):
    download_full_name = request.GET.get("download_full_name")
    
    ### File_Util 클래스 생성하기
    fu = File_Util()

    ### 다운로드할 위치 : 전체경로 넣어주기
    fu.setDownload(download_full_name)

    ### 브라우저에서 파일 다운로드 시키기
    return fu.fileDownload()
    # return HttpResponse(download_full_name)


### include 연습 ####
def include_view(request):
    return render(request,
                  "thirdapp/include/include_view.html",
                  {})

### extends 연습 ####
def extends_view(request):
    cart_list = cart.getCartList()
    return render(request,
                  "thirdapp/extends/extends_view.html",
                  {"cart_list" : cart_list})