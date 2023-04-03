from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

### 최초 페이지
def index(request) :
    return render(request,
                  "mainapp/index.html",
                  {})
    # return HttpResponse("go go")