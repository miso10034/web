from nonmodelapp.model_db import db_sql

####### 주문(장바구니) 정보 관리 #######
def getCartList():
    
    sql = """
        select cart_member,cart_no, cart_prod, cart_qty
        from cart
    """
    return db_sql.getList(sql)

### 주문(장바구니) 상세정보 조회(1건 조회)
def getCartView(cart_no):
    sql = """
        select cart_member, cart_no, cart_prod, cart_qty
        from cart
        where cart_no = '{}'
    """.format(cart_no)

    return db_sql.getView(sql)
    
### 주문(장바구니) 수정 처리하기
def setCartUpdate(cart_no, cart_prod, cart_qty):
    sql = """
        update cart
            set cart_prod = '{}'
                cart_qty = '{}'
        where cart_no = '{}'
    """.format(cart_no, cart_prod, cart_qty)

    return db_sql.setUpdate(sql)
    

