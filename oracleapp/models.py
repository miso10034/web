from django.db import models
### 데이터타입 라이브러리 정의
# - DB에서 varchar2 또는 char 등 문자열 타입
from django.db.models.fields import CharField
# - DB에서 number 또는 integer 등 숫자형 타입
from django.db.models.fields import IntegerField
# Create your models here.

### models.py에 클래스가 추가되는 경우 무조건 아래 명령 실행
# >python manage.py makemigrations oracleapp
# >python manage.py migrate


### 실제 DB에 있는 테이블의 형상과 동일하게 생성하기
# - 테이블명, 컬럼명은 실제 이름과 동일하게 작성해야함
# - 테이블은 class로 생성, 컬럼명은 변수로 정의

### 회원정보 테이블
class Member(models.Model) :
    mem_id = CharField(primary_key=True,
                       max_length=15, null=False)
    mem_pass = CharField(max_length=15, null=False)
    mem_name = CharField(max_length=20, null=False)
    mem_add1 = CharField(max_length=100, null=False)

    ### 해당 클래스가 사용할 실제 테이블 및 앱 지정
    class Meta :
        ### 실제 사용할 테이블 이름 정의
        db_table = "member"

        ### 사용할 앱 이름 정의
        app_label = "oracleapp"

        ### 외부 데이터베이스에 테이블 존재여부 확인
        # - 존재하면 : False
        # - 존재하지 않으면 : True
        # --> 일반적으로 외부에 테이블을 생성한 후 개발이 진행됨
        managed = False

### 상품정보(prod) 테이블 클래스 생성하기

class Prod(models.Model):
    # 상품코드
    prod_id = CharField(primary_key=True, max_length=10, null=False)
    # 상품명
    prod_name = CharField(max_length=40, null=False)
    # 상품분류코드
    prod_lgu = CharField(max_length=4, null=False)
    # 거래처코드
    prod_buyer = CharField(max_length=6, null=False)
    # 매입가
    prod_cost = IntegerField(max_length=10, null=False)
    # 소비자가
    prod_price = IntegerField(max_length=10, null=False)
    # 판매가
    prod_sale = IntegerField(max_length=10, null=False)

    class Meta:
        ### 실제 사용할 테이블 이름 정의
        db_table ="prod"

        ### 사용할 앱 이름 정의
        app_label="oracleapp"

        ### 외부 데이터베이스에 테이블 존재여부 확인
        # - 존재하면 : False
        # - 존재하지 않으면 : True
        # --> 일반적으로 외부에 테이블을 생성한 후 개발이 진행됨
        managed=False

					

### 주문정보(장바구니) chart 테이블 클래스 생성하기
class Cart(models.Model) : 
    ### member 테이블과 cart 테이블 연결하기(Member=Cart)
    #   관계조건 : member.mem_id = cart.cart_member
    #   클래스 조건 : Member.mem_id = Cart.cart_member
    # - 부모와 자식간의 관계(FK) 설정은 자식쪽에서 지정(Cart에서)
    # - 지정하는 컬럼은 실제 FK가 있는 컬럼의 변수를 이용
    
    ### ForeignKey 속성 설명
    # - Member : 참조할 부모 클래스 이름
    # - to_field : 참조할 부모 클래스의 PK 컬럼명(변수명)
    # - db_column : 자식 클래스에서 부모를 참조할 컬럼명(변수명)
    # - on_delete : 부모 데이터 삭제(delete)시 부모 데이터 처리 방법
    #             : PROTECT -> 부모를 참조하는 자식이 있다면,
    #                          삭제하지 않기(오류 발생 시킴)
    #             : CASCADE -> 부모와 관련된 자식 데이터 모두 삭제 시킴
    #                           (부모와의 관계를 일시적으로 차단시킴)
    cart_member = CharField(max_length=15, null=False)
    # cart_member = models.ForeignKey(Member,
    #                                 to_field="mem_id",
    #                                 db_column="cart_member",
    #                                 on_delete=models.PROTECT)
    # foreignkey로 접근하게 되면 객체자체가 들어옴

    ### cart_no만 PK로 지정
    cart_no = CharField(primary_key = True, max_length=13, null=False)
    cart_prod = CharField(max_length=10, null=False)
    cart_qty = IntegerField(max_length=8, null=False)

    class Meta : 
        db_table = "cart"
        app_label="oracleapp"
        managed = False
        
### 주문정보(장바구니) chart 테이블 클래스 생성하기        
class MemCart(models.Model) : 
    ### member 테이블과 cart 테이블 연결하기(Member=Cart)
    #   관계조건 : member.mem_id = cart.cart_member
    #   클래스 조건 : Member.mem_id = Cart.cart_member
    # - 부모와 자식간의 관계(FK) 설정은 자식쪽에서 지정(Cart에서)
    # - 지정하는 컬럼은 실제 FK가 있는 컬럼의 변수를 이용
    
    ### ForeignKey 속성 설명
    # - Member : 참조할 부모 클래스 이름
    # - to_field : 참조할 부모 클래스의 PK 컬럼명(변수명)
    # - db_column : 자식 클래스에서 부모를 참조할 컬럼명(변수명)
    # - on_delete : 부모 데이터 삭제(delete)시 부모 데이터 처리 방법
    #             : PROTECT -> 부모를 참조하는 자식이 있다면,
    #                          삭제하지 않기(오류 발생 시킴)
    #             : CASCADE -> 부모와 관련된 자식 데이터 모두 삭제 시킴
    #                           (부모와의 관계를 일시적으로 차단시킴)
    # cart_member = CharField(max_length=15, null=False)
    cart_member = models.ForeignKey(Member,
                                    to_field="mem_id",
                                    db_column="cart_member",
                                    on_delete=models.PROTECT)
    # foreignkey로 접근하게 되면 객체자체가 들어옴

    ### cart_no만 PK로 지정
    cart_no = CharField(primary_key = True, max_length=13, null=False)
    cart_prod = CharField(max_length=10, null=False)
    cart_qty = IntegerField(max_length=8, null=False)

    class Meta : 
        db_table = "cart"
        app_label="oracleapp"
        managed = False

### 주문(장바구니) + 회원정보 + 상품정보 연결
class CartMemProd(models.Model):
    cart_member = models.ForeignKey(Member,
                                    to_field="mem_id",
                                    db_column="cart_member",
                                    on_delete=models.PROTECT)
    cart_no = CharField(primary_key = True, max_length=13, null=False)
    cart_prod = models.ForeignKey(Prod,
                                    to_field="prod_id",
                                    db_column="cart_prod",
                                    on_delete=models.PROTECT)
    cart_qty = IntegerField(max_length=8, null=False)

    class Meta : 
        db_table = "cart"
        app_label="oracleapp"
        managed = False
    

