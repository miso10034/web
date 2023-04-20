from nonmodelapp.model_db_class import db_sql

### 상품분류정보 전체 조회하기
def getLprodList():
    ### SQL 구문 만들기
    sql = """
        select lprod_gu, lprod_nm 
        from lprod
        Order By lprod_nm ASC
    """
    return db_sql.getList(sql)
