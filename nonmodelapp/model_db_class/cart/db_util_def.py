### 오라클 라이브러리 불러들이기
import cx_Oracle

##### - DB접속 기능 함수 정의
def getDBConn_Cursor() :
    dsn = cx_Oracle.makedsn("localhost", 1521, "xe")
    conn = cx_Oracle.connect("gwangju_a", "dbdb", dsn)
    cursor = conn.cursor()
    
    return conn, cursor



##### - 조회결과에서 컬럼명 추출하기 기능 정의
def getColName(cursor):
    col = []
    for t in cursor.description :
        # col 리스트 변수에 값을 추가하기 : append(값) 사용
        col.append(t[0].lower())
    return col



##### - "한건 조회" 시 딕셔너리로 변환하는 기능 정의
def getFetchOne(cursor, row) :
    # 컬럼명 조회 함수 호출
    col = getColName(cursor)
    
    dict_row = {}
    for i in range(0, len(col), 1) :
        dict_row[col[i]] = row[i]
        
    return dict_row



##### - "여러건 조회" 시 리스트의 딕셔너리로 변환하는 기능 정의
def getFetchAll(cursor, rows) :
    # 컬럼명 조회 함수 호출
    col = getColName(cursor)
    
    list_row = []
    for t in rows:
        dict_temp = {}
        for i in range(0, len(col), 1):
            dict_temp[col[i]] = t[i]
        list_row.append(dict_temp)
        
    return list_row


##### - 커서 및 connect 접속 해제하는 기능 정의
def DBClose(cursor, conn) :
    ### 커서(cursor) 반환하기
    cursor.close()
    
    ### 접속(connect) 접속 해제
    conn.close()