from django.contrib import admin
from django.urls import path, include

from mainapp import views
# from firstapp import views as v1
# from secondapp import views as v2
### from 뒤에 작성규칙
#  - 폴더 경로 또는 폴더 경로 + 파일명
###

urlpatterns = [
    ### http://127.0.0.1:8000/
    path('', views.index),
    ### http://127.0.0.1:8000/index
    path('index/', views.index),
    
    # http://127.0.0.1:8000/first/
    path('first/', include('firstapp.urls')),
    
    # http://127.0.0.1:8000/second/
    path('second/', include('secondapp.urls')),

    # http://127.0.0.1:8000/main/
    path('main/', include('mainapp.urls')),

    # http://127.0.0.1:8000/front/
    path('front/', include('frontapp.urls')),

    path('admin/', admin.site.urls),
]
