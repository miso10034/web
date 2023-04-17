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
    path('mem_update/', views.getMemUpdateForm),

    ############# [주문(장바구니) 관리] ###############
    ### http://127.0.0.1:8000/nonmodel/cart_list/
    path('cart_list/', views.getCartList),
    ### http://127.0.0.1:8000/oracle/cart_view/
    path('cart_view/', views.getCartView),
    ### http://127.0.0.1:8000/nonmodel/cart_update/
    path('cart_update/', views.getCartUpdate),
]
