from thirdapp.model_db_class.db_util_def import DB_Util

def getList(sql):
    db_util = DB_Util()
    list_row = db_util.getFetchAll(sql)
    return list_row

def getView(sql):
    db_util = DB_Util()
    dict_row = db_util.getFetchOne(sql)
    return dict_row

def setCUD(sql):
    db_util = DB_Util()
    db_util.setCUD(sql)

    return "ok"