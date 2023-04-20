### 발송시키는 라이브러리 ####
# - EmailMessage django에서 지원하는 메일을 발송시키는 라이브러리 호출

from django.core.mail import EmailMessage

### 이메일 발송하기
def sendEmail(emails, title, content) : 
    email = EmailMessage(
        ### 이메일 제목
        title, 
        ### 이메일 내용
        content,
        ### 받는 사람 이메일
        # - 여러명에게 보낼 경우에는 콤마로 구분하여 폼에서 작성
        to = [emails], 
        
    )# 여기까지 생성자

    ### 이메일 전송하기
    # 성공여부 : 성공(1), 실패(0)
    send_chk = email.send()

    return send_chk