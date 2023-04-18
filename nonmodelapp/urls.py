from django.urls import path
from . import views

urlpatterns = [
    ### http://127.0.0.1:8000/nonmodel
    path('', views.index),
    ### http://127.0.0.1:8000/nonmodel/index
    path('index/', views.index),

    ############ 회원관리 ################
    ### http://127.0.0.1:8000/nonmodel/mem_list/
    path('mem_list/', views.getMemberList),
    ### http://127.0.0.1:8000/nonmodel/mem_view/
    path('mem_view/', views.getMemberView),
    ### http://127.0.0.1:8000/nonmodel/mem_update_form/
    path('mem_update_form/', views.getMemUpdateForm),
    ### http://127.0.0.1:8000/nonmodel/mem_update/
    path('mem_update/', views.getMemUpdate),

    # ############# [주문(장바구니) 관리] ###############
    # ### http://127.0.0.1:8000/nonmodel/cart_list/
    # path('cart_list/', views.getCartList),
    # ### http://127.0.0.1:8000/oracle/cart_view/
    # path('cart_view/', views.getCartView),
    # ### http://127.0.0.1:8000/nonmodel/cart_update_form/
    # path('cart_update_form/', views.setCartUpdateForm),
    
    ############### 로그인 처리 #####################
    ### http://127.0.0.1:8000/nonmodel/login_form/
    path('login_form/', views.login_form),
    ### http://127.0.0.1:8000/nonmodel/login_chk/
    path('login_chk/', views.login_chk),
    ### http://127.0.0.1:8000/nonmodel/logout_chk/
    path('logout_chk/', views.logout_chk),
]
