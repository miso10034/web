
from django.urls import path
from . import views

urlpatterns = [
    ### http://127.0.0.1:8000/third
    path('', views.index),
    ### http://127.0.0.1:8000/third/index
    path('index/', views.index),
    
    ############# [주문(장바구니) 관리] ###############
    ### http://127.0.0.1:8000/third/cart_list/
    path('cart_list/', views.getCartList),
    ### http://127.0.0.1:8000/third/cart_view/
    path('cart_view/', views.getCartView),
    ### http://127.0.0.1:8000/third/cart_update_form/
    path('cart_update_form/', views.getCartUpdateForm),
    ### http://127.0.0.1:8000/third/cart_update/
    path('cart_update/', views.getCartUpdate),
    ### http://127.0.0.1:8000/third/cart_insert/
    path('cart_insert_form/', views.getCartInsertForm),
    ### http://127.0.0.1:8000/third/cart_insert/
    path('cart_insert/', views.getCartInsert),
    ### http://127.0.0.1:8000/third/cart_delete/
    path('cart_delete/', views.getCartDelete),

    ########### 상세 ############
    ### http://127.0.0.1:8000/third/search_prod/
    path('search_prod/', views.getSearchProd),
]
