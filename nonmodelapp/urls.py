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

    ############# [주문(장바구니) 관리] ###############
    ### http://127.0.0.1:8000/nonmodel/cart_list/
    path('cart_list/', views.getCartList),
    ## http://127.0.0.1:8000/nonmodel/cart_view/
    path('cart_view/', views.getCartView),
    ### http://127.0.0.1:8000/nonmodel/cart_update_form/
    path('cart_update_form/', views.getCartUpdateForm),
    ### http://127.0.0.1:8000/nonmodel/cart_update/
    path('cart_update/', views.getCartUpdate),
    ### http://127.0.0.1:8000/nonmodel/cart_insert_form/
    path('cart_insert_form/', views.getCartInsertForm),
    ### http://127.0.0.1:8000/nonmodel/cart_insert/
    path('cart_insert/', views.getCartInsert),
    ### http://127.0.0.1:8000/nonmodel/cart_delete/
    path('cart_delete/', views.getCartDelete),
    
    ############### 로그인 처리 #####################
    ### http://127.0.0.1:8000/nonmodel/login_form/
    path('login_form/', views.login_form),
    ### http://127.0.0.1:8000/nonmodel/login_chk/
    path('login_chk/', views.login_chk),
    ### http://127.0.0.1:8000/nonmodel/logout_chk/
    path('logout_chk/', views.logout_chk),

    ############### 검색에 의한 상품상세조회 처리 #####################
    ### http://127.0.0.1:8000/nonmodel/search_prod/
    path('search_prod/', views.getSearchProd),

    ############### 이메일 발송 처리 #####################
    ### http://127.0.0.1:8000/nonmodel/email_form/
    path('email_form/', views.getEmailForm),
    ### http://127.0.0.1:8000/nonmodel/email_send/
    path('email_send/', views.emailSend),

    ############# 페이징 처리 ###############
    ### http://127.0.0.1:8000/nonmodel/cart_list_page/
    path('cart_list_page/', views.getCartListPaging),

    ############# File Up/Download 처리 ###############
    ### http://127.0.0.1:8000/nonmodel/file_insert_form/
    path('file_insert_form/', views.getFileInsertForm),
    ### http://127.0.0.1:8000/nonmodel/file_insert/
    path('file_insert/', views.setFileInsert),
    ### http://127.0.0.1:8000/nonmodel/file_down/
    path('file_down/', views.setFileDown),

    ############# 페이지 코드 포함(include) 처리 ###############
    ### http://127.0.0.1:8000/nonmodel/include_view/
    path('include_view/', views.include_view),
    ### http://127.0.0.1:8000/nonmodel/include_view2/
    path('include_view2/', views.include_view2),

    ############# 페이지 실행 결과 포함(extends) 처리 ###############
    ### http://127.0.0.1:8000/nonmodel/extends_view/
    path('extends_view/', views.extends_view),
    ### http://127.0.0.1:8000/nonmodel/block_view1/
    path('block_view1/', views.block_view1),
    ### http://127.0.0.1:8000/nonmodel/block_view2/
    path('block_view2/', views.block_view2),
    ### http://127.0.0.1:8000/nonmodel/block_view3/
    path('block_view3/', views.block_view3),
    ### http://127.0.0.1:8000/nonmodel/block_mem_list/
    path('block_mem_list/', views.block_mem_list),
   
    ############# 비동기방식(jquery) 처리 ###############
    ### http://127.0.0.1:8000/nonmodel/load_view/
    path('load_view/', views.load_view),
    ### http://127.0.0.1:8000/nonmodel/load_view1/
    path('load_view1/', views.load_view1),
    ### http://127.0.0.1:8000/nonmodel/load_view2/
    path('load_view2/', views.load_view2),
    ### http://127.0.0.1:8000/nonmodel/load_view3/
    path('load_view3/', views.load_view3),

    ############# 지도 시각화 ###############
    ### http://127.0.0.1:8000/nonmodel/map_view/
    path('map_view/', views.map_Visualization),

    ############# 데이터 시각화 ###############
    ### http://127.0.0.1:8000/nonmodel/data_view/
    path('data_view/', views.data_Visualization),

    ############# [머신러닝 모델 연동 ] ###############
    ### http://127.0.0.1:8000/nonmodel/ml_view/
    path('ml_view/', views.getML_View),
]
