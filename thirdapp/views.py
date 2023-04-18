from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,
                  "thirdapp/index.html",{})

def getCartList(request):
    return render(request,
                  "thirdapp/cart_list.html",{})

def getCartView(request):
    return render(request,
                  "thirdapp/cart_view.html",{})

def setCartUpdate(request):
    return render(request,
                  "thirdapp/cart_update_form.html",{})

def getLoginChk(request):
    return render(request,
                  "thirdapp/login/login_form.html",{})
