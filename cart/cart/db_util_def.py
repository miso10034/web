### 오라클 라이브러리 불러들이기
import cx_Oracle

##### - DB접속 기능 함수 정의

class DB_Util1 :

    def __init__(self):
        self.getDBConn_Cursor()

    def getDBConn_Cursor(self) :
        dsn = cx_Oracle.makedsn("localhost", 1521, "xe")
        self.conn = cx_Oracle.connect("gwangju_a", "dbdb", dsn)
        self.cursor = self.conn.cursor()

    ##### - 조회결과에서 컬럼명 추출하기 기능 정의
    def getColName(self):
        col = []
        for t in self.cursor.description :
            # col 리스트 변수에 값을 추가하기 : append(값) 사용
            col.append(t[0].lower())
        return col



    ##### - "한건 조회" 시 딕셔너리로 변환하는 기능 정의
    def getFetchOne(self, sql) :

        ### 구문 실행하기
        self.cursor.execute(sql)

        ### 결과 추출하기
        row = self.cursor.fetchall()

        # 컬럼명 조회 함수 호출
        col = self.getColName()
        
        dict_row = {}
        for i in range(0, len(col), 1) :
            dict_row[col[i]] = row[i]
        ### DB 접속 해제하기
        self.DBClose()   
        return dict_row



    ##### - "여러건 조회" 시 리스트의 딕셔너리로 변환하는 기능 정의
    def getFetchAll(self, sql) :

        ### 구문 실행하기
        self.cursor.execute(sql)

        ### 결과 추출하기
        rows = self.cursor.fetchall()

        # 컬럼명 조회 함수 호출
        col = self.getColName()
        
        list_row = []
        for t in rows:
            dict_temp = {}
            for i in range(0, len(col), 1):
                dict_temp[col[i]] = t[i]
            list_row.append(dict_temp)

        self.DBClose()     
        return list_row
    
    def setCUD(self, sql):
        ### 구문 실행하기
        self.cursor.execute(sql)
        
        ### 데이터 수정/삭제/입력시에 아래 적용해야함
        self.conn.commit()

        ### DB 접속 해제하기
        self.DBClose()


    ##### - 커서 및 connect 접속 해제하는 기능 정의
    def DBClose(self) :
        ### 커서(cursor) 반환하기
        self.cursor.close()
        
        ### 접속(connect) 접속 해제
        self.conn.close()