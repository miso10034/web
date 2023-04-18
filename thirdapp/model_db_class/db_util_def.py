import cx_Oracle

class DB_Util:
    def __init__(self):
        self.getDBConn_Cursor()

    def getDBConn_Cursor(self):
        dsn = cx_Oracle.makedsn("localhost", 1521, "xe")
        self.conn = cx_Oracle.connect("gwangju_a", "dbdb", dsn)
        self.cursor = self.conn.cursor()

    def getColName(self):
        col = []
        for t in self.cursor.description : 
            col.append(t[0].lower())
        return col
    
    def getFetchOne(self, sql):
        try:
            self.cursor.execute(sql)

            row = self.cursor.fetchone()

            if row == None:
                self.DBClose()
                return {"RS":"Data_None"}
            
            col = self.getColName()

            dict_row = {}
            for i in range(0, len(col), 1):
                dict_row[col[i]] = row[i]
            
            self.DBClose()
        except:
            self.DBClose()
            return {"RS":"DB_ERROR"}
        return dict_row
    
    def getFetchAll(self, sql):
        try:
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()

            if rows == None:
                self.DBClose()
                return [{"RS": "Data_None"}]
            
            col = self.getColName()

            list_row = []
            for t in rows:
                dict_temp = {}
                for i in range(0, len(col), 1):
                    dict_temp[col[i]] = t[i]
                list_row.append(dict_temp)

            self.DBClose()
        except:
            self.DBClose()
            return [{"RS": "DB_ERROR"}]
        return list_row
    
    def setCUD(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()
        self.DBClose()

    def DBClose(self):
        self.cursor.close()
        self.conn.close()

