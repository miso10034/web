from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields import IntegerField

### 파일 테스트
# - Table 생성 : file_tb
# - 컬럼 :no, title, img_full_name, download_full_name
#       : no는 pk
class File_tb(models.Model):
    no = CharField(primary_key=True, null=False)
    title = CharField(max_length=20, null=False)
    img_full_name = CharField(max_length=20, null=False)
    download_full_name = CharField(max_length=20, null=False)

    class Meta : 
        db_table = "File_tb"
        app_label = "thirdapp"
        managed = False