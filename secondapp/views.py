from django.shortcuts import render
from django.http import HttpResponse
from .models import Cart

def second(request) :
    return HttpResponse("second 호출....")

def index(request) :
    return render(request,
                  "secondapp/index.html")

def getCartList(request):
    '''
        select * from cart;
    '''
    cart_list = Cart.objects.all().order_by("-cart_no")
    
    return render(request,
                  "secondapp/cart/cart_list.html",
                  {"cart_list" : cart_list})

def getCartView(request):

    cart_no = request.GET.get("cart_no","error")
    cart_prod = request.GET.get("cart_prod","error")

    cart_view = Cart.objects.get(cart_no = cart_no,
                                 cart_prod = cart_prod)
    return render(request,
                  "secondapp/cart/cart_view.html",
                  {"cart_no":cart_no,
                   "cart_prod":cart_prod,
                   "cart_view":cart_view})

def getCartUpdateForm(request):
    cart_no = request.GET.get("cart_no", "error")
    cart_prod = request.GET.get("cart_prod","error")

    cart_view = Cart.objects.get(cart_no=cart_no,
                                 cart_prod = cart_prod)
    return render(request,
                  "secondapp/cart/cart_update_form.html",
                  {"cart_no" : cart_no,
                   "cart_prod" : cart_prod,
                   "cart_view" : cart_view})

def getCartUpdate(request):

    cart_no = request.POST.get("cart_no","Error")
    cart_prod = request.POST.get("cart_prod","Error")
    cart_qty = request.POST.get("cart_qty","Error")

    Cart.objects.filter(cart_no=cart_no,
                        cart_prod=cart_prod).update(cart_qty=cart_qty)
    
    msg = """
            <script type="text/javascript">
                alert("정상작동");
                location.href = '/oracle/cart_view/?cart_no={}&cart_prod={}';
    """.format(cart_no,cart_prod)
    return HttpResponse(msg)