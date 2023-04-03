from django.contrib import admin
from django.urls import path, include

from mainapp import views
# from firstapp import views as v1
# from secondapp import views as v2

### from 뒤에 작성규칙
#  - 폴더 경로 또는 폴더 경로 + 파일명
### import 뒤에 작성규칙
#  * from에서 폴더경로까지만 지정한 경우
#  - 파일명 (무조건 파일명은 소문자)
#  * from에서 파일명까지 지정한 경우
#    - 클래스명(대문자로 시작) 또는 함수명


### http://127.0.0.1:8000/url경로/
### path('url경로',함수이름)
urlpatterns = [
    ### http://127.0.0.1:8000/
    path('', views.index),
    ### http://127.0.0.1:8000/index
    path('index/', views.index),
 
    # http://127.0.0.1:8000/first/
    path('first/', include('firstapp.urls')),
    
    # http://127.0.0.1:8000/second/
    path('second/', include('secondapp.urls')),

    path('admin/', admin.site.urls),
]
