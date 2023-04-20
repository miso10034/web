from thirdapp.model_db_class import db_sql

### 회원 전체 조회하기
def getCartList():

    ### 구문 작성
    # - 전체조회시 * 보다는 컬럼명을 전부 타이핑하는 것이 맞음
    sql = """
        select cart_no, cart_member, cart_prod, cart_qty
        From cart
        Order By cart_no Desc
    """
    return db_sql.getList(sql)

### 한건 조회하기
def getCart(cart_no,cart_prod):

    ### 구문 작성
    sql = """
        select cart_no, cart_member, cart_prod, cart_qty
        From cart
        Where cart_no = '{}'
            AND cart_prod = '{}'
    """.format(cart_no,cart_prod)

    return db_sql.getView(sql)

### 수정처리하기
def setCartUpdate(cart_no, cart_prod, cart_qty):

    ### 구문 작성
    sql = """
        Update cart
            Set cart_qty = {}
        Where cart_no = '{}'
            and cart_prod = '{}'
    """.format(cart_qty,cart_no, cart_prod)

    return db_sql.setCUD(sql)

### 입력 처리하기
def setCartInsert(cart_no, cart_prod, cart_qty, cart_member):

    ### 구문 작성
    sql = """
        insert into cart (
            cart_no, cart_prod, cart_qty, cart_member
        ) values (
            '{}', '{}', {}, '{}'
        )
    """.format(cart_no, cart_prod, cart_qty, cart_member)

    return db_sql.setCUD(sql)

### 삭제 처리하기
def setCartDelete(cart_no, cart_prod):

    ### 구문 작성
    sql = """
        Delete From cart
        Where cart_no = '{}'
            and cart_prod = '{}'
    """.format(cart_no, cart_prod)

    return db_sql.setCUD(sql)

