from django.shortcuts import render

# Create your views here.
### 최초 페이지 
def index(request) :
    return render(request,
                  "frontapp/index.html",
                  {})

### 이미지 보여주기
def imageView(request) :
    return render(request,
                  "frontapp/01_image.html",
                  {})

### CSS 테스트-1
def cssView1(request):
    return render(request,
                  "frontapp/02_css1.html",
                  {})

### CSS 테스트-2
def cssView2(request):
    return render(request,
                  "frontapp/02_css2.html",
                  {})

### CSS 테스트-2
def cssView3(request):
    return render(request,
                  "frontapp/02_css3.html",
                  {})

### javascript 테스트-1
def javascriptView1(request):
    return render(request,
                  "frontapp/01_javascript1.html",
                  {})

### javascript 테스트-1
def javascriptView2(request):
    return render(request,
                  "frontapp/01_javascript2.html",
                  {})

###### [HTML] ######
def htmlView01(request) :
    return render(request,
                  "frontapp/html/01_html.html",
                  {})
# 리턴값을 urls.py에게 넘겨줌
# render 사용자정보 데이터 정보를 읽어드린다음 필요한것을 처리해서 리턴

def linkView(request):
    return render(request,
                  "frontapp/html/01_link.html",
                  {})

def linkView2(request):
    return render(request,
                  "frontapp/html/02_link.html",
                  {})

def linkView3(request) :
    return render(request,
                  "frontapp/html/03_link.html",
                  {})

def cssView(request):
    return render(request,
                  "frontapp/html/04_css.html",
                  {})

def tableView(request):
    return render(request,
                  "frontapp/html/05_table.html",
                  {})

def tableView2(request):
    context = {"id"  :"a001",
                "name":"김지연",
                "addr":"전주 만성동 과수원"}
    c_list = [context, context, context]
    return render(request,
                  "frontapp/html/06_table.html",
                  {"c_list" : c_list})

def ulView(request):
    return render(request,
                  "frontapp/html/07_ul.html",
                  {})

def divView(request):
    return render(request,
                  "frontapp/html/08_div.html",
                  {})

def divView2(request):
    return render(request,
                  "frontapp/html/09_div.html",
                  {})

def iframeView(request):
    return render(request,
                  "frontapp/html/10_iframe.html",
                  {})

def cssTableView(request):
    return render(request,
                  "frontapp/css/01_cssTable.html",
                  {})

def cssTableView2(request) :
    context = {"id" : "a001",
               "name" : "홍길동1",
               "addr" : "광주 소촌동 1-1"}
    context2 = {"id" : "a002",
               "name" : "홍길동2",
               "addr" : "광주 소촌동 1-2"}
    context3 = {"id" : "a003",
               "name" : "홍길동3",
               "addr" : "광주 소촌동 1-3"}
    context4 = {"id" : "a004",
               "name" : "홍길동4",
               "addr" : "광주 소촌동 1-4"}
    co_list = [context,context2,context3,context4]
    return render(request,
                  "frontapp/css/02_cssTable.html",
                  {"co_list" : co_list})
