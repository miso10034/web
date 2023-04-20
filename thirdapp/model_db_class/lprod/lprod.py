from thirdapp.model_db_class import db_sql

def getLprodList():
    sql = """
        select lprod_gu, lprod_nm
        from lprod
        order by lprod_nm asc
    """
    return db_sql.getList(sql)