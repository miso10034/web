from nonmodelapp.model_db_class import db_sql

### 상품분류정보 전체 조회하기
def getSelBox_Lprod():
    ### SQL 구문 만들기
    sql = """
        select Distinct lprod_gu, lprod_nm 
        from lprod, prod
        where lprod_gu = prod_lgu
        Order By lprod_nm ASC
    """
    return db_sql.getList(sql)


### 선택된 상품분류에 대한 상품 정보 조회하기
# - 상품 selectbox에 넣을 값 조회
def getSelBox_Lprod_Prod(lprod_gu) :
    ### SQL 구문 만들기
    sql = """
        Select prod_id, prod_name
        from lprod, prod
        where lprod_gu = prod_lgu
          And lprod_gu = '{}'
        Order By prod_name asc
    """.format(lprod_gu)

    return db_sql.getList(sql)

### 선택된 상품분류 및 상품에 대한 
# - 상품 상세조회하기 처리
def getLprod_Prod_Buyer(lprod_gu, prod_id):
    ### sql 구문작성
    sql = """
        select lprod_nm,
        prod_name, prod_sale,
        buyer_name, buyer_add1
        from lprod, prod, buyer
        where lprod_gu = prod_lgu
        and buyer_id = prod_buyer
        and lprod_gu = '{}'
        and prod_id = '{}'
    """.format(lprod_gu, prod_id)

    return db_sql.getView(sql)