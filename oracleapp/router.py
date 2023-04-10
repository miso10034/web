### Database 추가시 아래 클래스를 APP에 router.py 추가해야함
# - return or db에는 : mysql 입력(settings.py에 설정하 DB 이름)
# - app_label에는 : mysqlapp 이름 지정
class DBRouter:
    def db_for_read(self, model, **hints):
        # app_label -> 내가 지정하는 app
        if model._meta.app_label=='oracleapp': 
            return'oracle' 
            # settings.py에 지정한 오라클 데이터베이스 추가한 것
        return None
    
    # db_for_write -> 조회하는 함수
    def db_for_write(self, model, **hints): 
        if model._meta.app_label=='oracleapp':
            return'oracle'
        return None

    # allow_relation ->관계설정하는 함수
    def allow_relation(self, obj1, obj2, **hints): 
        if obj1._meta.app_label=='oracleapp'or\
            obj2._meta.app_label=='oracleapp':
            return True
        return None
    
    # 내가 만든 형상과 일치하는 지 확인하는 함수
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label=='oracleapp':
            return db=='oracle'
        return None
