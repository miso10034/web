### 오라클 라이브러리 불러들이기
import cx_Oracle

### 클래스 내부의 모든 함수에는 매개변수 self 키워드를 넣어야 합니다.(규칙)
# - self : self가 표시된 변수들은 전역변수 또는 외부파일에서 직접 접근이 가능하게됨
# - class 내부의 함수간의 호출을 위해서는 self를 붙여야 합니다.
class DB_Util :

    ### 생성자 정의하기
    def __init__(self):
        ### - 클래스 생성과 동시에 DB 연결 및 커서 받아오는 기능 수행
        self.getDBConn_Cursor() 

    ##### - DB접속 기능 함수 정의
    def getDBConn_Cursor(self):
        dsn = cx_Oracle.makedsn("localhost", 1521, "xe")
        self.conn = cx_Oracle.connect("gwangju_a", "dbdb", dsn)
        self.cursor = self.conn.cursor()
        # conn, cursor를 외부에서도 사용할 수 있는 전역변수로 만들어주기 위해 self를 붙여줌
        # 전역변수로 선언했기 때문에 return값은 없어도 된다.



    ##### - 조회결과에서 컬럼명 추출하기 기능 정의
    def getColName(self): # 매개변수 cursor 삭제 : cursor가 전역변수이기 때문에
        col = []
        for t in self.cursor.description :
            # col 리스트 변수에 값을 추가하기 : append(값) 사용
            col.append(t[0].lower())
        return col



    ##### - "한건 조회" 시 딕셔너리로 변환하는 기능 정의
    def getFetchOne(self, sql) :
        try:

            ### 구문 실행하기
            self.cursor.execute(sql)

            ### 결과 추출하기
            row = self.cursor.fetchone()

            ### 조회 결과가 없을 때 처리하기
            if row == None:
                self.DBClose()
                return {"RS": "Data_None"}

            # 컬럼명 조회 함수 호출
            # 함수 호출해야해서 self를 붙여줌
            col = self.getColName() 
           
            dict_row = {}
            for i in range(0, len(col), 1) :
                dict_row[col[i]] = row[i]
            
            self.DBClose()
        except:
            self.DBClose()
            return {"RS": "DB_ERROR"}
        
        return dict_row



    ##### - "여러건 조회" 시 리스트의 딕셔너리로 변환하는 기능 정의
    def getFetchAll(self, sql) :
        try:

            ### 구문 실행하기
            self.cursor.execute(sql)
            # . : 클래스의 주소로 접근해라 그 안에 있는 cursor를 사용할거야

            ### 결과 추출하기
            rows = self.cursor.fetchall()
            
            ### 조회 결과가 없을 때 처리하기
            if rows == None:
                self.DBClose()
                return [{"RS": "Data_None"}]
            
            # 컬럼명 조회 함수 호출
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

    ##### - 데이터 입력(C), 수정(U), 삭제(D) 처리 기능 정의
    def setCUD(self, sql):
        ### 구문 실행하기
        self.cursor.execute(sql)
        
        ### 데이터 수정/삭제/입력시에 아래 적용해야함
        self.conn.commit()

        ### DB 접속 해제하기
        self.DBClose()


    ##### - 커서 및 connect 접속 해제하는 기능 정의
    def DBClose(self) : # 매겨변수 cursor, conn 삭제
        ### 커서(cursor) 반환하기
        self.cursor.close() # self로 접근
        
        ### 접속(connect) 접속 해제
        self.conn.close()
        