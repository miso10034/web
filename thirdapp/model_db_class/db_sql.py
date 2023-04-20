from thirdapp.model_db_class.db_util_def import DB_Util 
                                              #   클래스명
# 한번 쓰고 기능이 종료되서 class로 만들 필요가 없음

### 여러건 조회하기
def getList(sql):
    ### 클래스 생성시키기
    # 클래스 생성과 동시에 conn정보와 cursor 정보를 가지고 있음(db_util_def 파일에서)
    # - 클래스 내에 변수들은 별도로 받아오지 않아도 되며, 직접 접근가능함
    db_util = DB_Util() # = 할당연산자(주소값을 넘김)

    ### 딕셔너리로 변경하기
    list_row = db_util.getFetchAll(sql)
    return list_row

### 한건 조회하기
def getView(sql):
    ### 클래스 생성시키기
    db_util = DB_Util()
    # DB 접속 정보 받아오기 삭제 -> 클래스를 생성시켜서 DB_Util의 클래스를 호출시켜서 접속정보를 받아왔기 때문

    ### 딕셔너리로 변경하기
    dict_row = db_util.getFetchOne(sql)
    # print(dict_row)

    return dict_row

### 입력/수정/삭제 처리하기
def setCUD(sql):
    ### 클래스 생성하기
    db_util = DB_Util()

    # db_util_def에서 함수 setCUD호출
    db_util.setCUD(sql)

    return "ok :D"
