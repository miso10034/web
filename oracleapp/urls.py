from django.urls import path

### from 뒤에 작성규칙
#  - 폴더 경로 또는 폴더 경로 + 파일명
###

from . import views

urlpatterns = [
    ### http://127.0.0.1:8000/oracle/
    path('', views.index),
    ### http://127.0.0.1:8000/oracle/index/
    path('index/', views.index),

    ############ [회원관리] #########
    ### http://127.0.0.1:8000/oracle/mem_list/
    path('mem_list/', views.getMemberList),    
    ### http://127.0.0.1:8000/oracle/mem_view/
    path('mem_view/', views.getMemberView),

    ### http://127.0.0.1:8000/oracle/mem_update_form/
    path('mem_update_form/', views.getMemUpdateForm),

    ### http://127.0.0.1:8000/oracle/mem_update/
    path('mem_update/', views.getMemUpdate),
]
