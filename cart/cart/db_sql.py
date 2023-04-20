from nonmodelapp.model_db_class.db_util_def import DB_Util1

### 여러건 조회하기
def getList(sql):

    db_util = DB_Util1()

    ### 딕셔너리로 변경하기
    list_row = db_util.getFetchAll(sql)
    # print(dict_row)

    return list_row

### 회원 한건 조회하기
def getView(sql):
    
    db_util = DB_Util1()

    ### 딕셔너리로 변경하기
    dict_row = db_util.getFetchOne(sql)
    # print(dict_row)

    return dict_row

### 수정처리하기
def setCUD(sql):
    
    db_util = DB_Util1()

    db_util.setCUD(sql)
    
    return "ok :D"
