from thirdapp.model_db_class import db_sql

def getSelBox_Lprod():
    sql = """
        select Distinct lprod_gu, lprod_nm
        from lprod, prod
        where lprod_gu = prod_lgu
        order by lprod_nm asc
    """
    return db_sql.getList(sql)

def getSelBox_Lprod_prod(lprod_gu):
    sql = """
        select prod_id, prod_name
        from lprod, prod
        where lprod_gu = prod_lgu
          and lprod_gu = '{}'
        order by prod_name asc 
    """.format(lprod_gu)

    return db_sql.getList(sql)

def getLprod_Prod_Buyer(lprod_gu, prod_id):
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