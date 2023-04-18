from thirdapp.model_db_class import db_sql
# cart_member, cart_no, cart_prod, cart_qty
def getCartList():
    sql="""
        select cart_member, cart_no, cart_prod, cart_qty
        from cart
    """
    return db_sql.getList(sql)

def getCartView(cart_no):
    sql="""
        select cart_member, cart_no, cart_prod, cart_qty
        from cart
        where cart_no = '{}'
    """.format(cart_no)
    return db_sql.getView(sql)

def setCartUpdate(cart_prod, cart_qty, cart):
    sql = """
        update cart
            set cart_prod = '{}',
                cart_qty = '{}'
        where cart_no = '{}'
    """.format(cart_prod, cart_qty, cart)
    return db_sql.setCUD(sql)

def getLoginChk(cart_id, cart_pass):
    sql="""
        select cart_member, cart_no, cart_prod, cart_qty
        from cart
        where cart_id = '{}'
            and cart_pass = '{}'
    """.format(cart_id,cart_pass)
    return db_sql.getView(sql)