# 불 자료형 / 참과 거짓 / 맨 앞은 무조건 대문자. 
a = True
print(a)

# 이런식으로 간단하게 트루 펄스 가능. 
a = 1==2 
print(a)

# 실제 프로그렘에서 어떻게 쓰이냐? / pop 은 하나 뽑아서 버린다 느낌 
# 반복문 
a = [1, 2, 3, 4]
while a:
    print(a)
    a.pop()

# 조건문 
if [1,2,3]:
    print("참")
else:
    print("거짓")

# 불연산 
a = bool([])
print(a)