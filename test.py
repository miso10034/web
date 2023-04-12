list_v2 = [{1:'홍길동1',2:'홍길동2'},
           {1:'이순신1',2:'이순신2'},
           {1:'강감찬1',2:'강감찬2'}]

print(list_v2)

for d in list_v2:
    print(d)
    for k in d:
        print("key:{}/ value:{}".format(k,d[k]))

# for 문으로 실행할 수 있는 4가지 -> 1.딕셔너리, 2.리스트 3. 튜플 4. 문자열
# 여러개를 넣을 수 있는 값들 -> for문 가능, index number 부여 가능
# for k in d.keys(); 형태로 딕셔너리 접근



# # "강감찬1"값이 있는 key와 value값만 출력해 주세요
# # 답 : key : 1 / value : 강감찬1
# # d.keys()
# # k=2 -> d[2] -> "강감찬1"
# for d in d.keys:
#     for k in d:
#         print("key:{2}/ value:{2}".format(k.d[k]))

# # "강감찬1"이라는 값이 포함되어 있는 부분의 딕셔너리의 전체 key와 value를 출력하기
# # 답 :
# # key : 1 / value : 강감찬1
# # key : 2 / value : 강감찬2
