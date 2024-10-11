# 정수형일때
a = 123 
print(type(a))

# 실수형일때 float 
a = 1.2 
print(type(a))

# 실수형 
a = 4.24E10
print(type(a))

#사칙연산 
a = 3 
b = 4 
c = 4 
print(a + b)
print(a * b)
# 몫을 구할때
print(c// b)
print(a ** b)

# 문자열 자료형 만드는 4가지 방법 
# c 같은 경우  " " 큰따옴표로 감싸지면 숫자여도 문자로 처리됨.
a = "Life is too short, You need Python"
b = "a"
c = "123"

# 큰따옴표 , 작은따옴표 뭘해도 가능함. 
 
# \n 줄바꿈 기호 
a = 'life is too short \nyou need python'
print(a) 

# \\ \를 그대로 표현할때 사용 
# \' 작은 따옴표를 그대로 표현할떄
# \" 큰따옴표를 그대로 표현할 떄 사용 

# 문자열 더해서 연결하기 
head = "python"
tail = " is fun !"
print(head + tail)
print(head*3)

# 문자열 곱하기 응용하기
print("=" * 50)
print("My Program")
print("=" * 50)

# 문자열 길이 구하기 length 의 약자 (len)
a = "life is too short"
print(len(a))

# 문자열 인덱싱과 슬라이싱 // l = 0 i = 1 f = 2 e = 3 // 항상 0 부터 시작하는걸 인지 해야할듯 
a = "Life is too short, You need Python"
print(a[3])
print(a[-1]) 

# 문자열 슬라이싱 
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)
c = a[0:4] # 4미만 미만의 개념이야 3까지 쓰기위해서 4를씀
print(c)
d = a[::] # 처음부터 끝까지를 의미 
print(d)
e = a[::2] # 두 칸 간격으로 뽑기 // 간격을 활용할떄 ::숫자 사용한다 생각 
print(e)

a = "20230331Rainy"
date = a[:8] # 처음부터 8 번 미만까지 
weather = a[8:] # 8번 초과 끝까지 
print(date)
print(weather)

# 문자열 포매팅 %d (decimal 십진수의) 
a = "I eat %d apples." % 3
print(a)  

# 포매팅 변수로 하기 
number = 3 
a = "I eat %d apples." % number 
print(a)

# 2개 이상의 값 넣기 
number = 10 
day = "three"
a = "I ate %d apples. so I was sick for %s days." % (number, day)
print(a)

# %s는 어떠한 것 도 가능함 ~~ 개꿀!

# 포맷 코드와 숫자 함께 사용하기
# 정렬과 공백 // 전체 길이가 10개인 문자열 공간에서 오른쪽으로 정렬 느낌 8칸 점프!
a = "%10s" % "hi"
print(a)

# 소수점 표현하기 // 소수점 4쨰자리까지 표현해!
a = "%0.4f" % 3.42134234
print(a)

#숫자 값을 가진 변수로 대입하기 // number가 0 번째 day가 1번쨰 
number = 10
day = "three"
a = "I ate {0} apples. so I was sick for {1} days.".format(number, day)
print(a)

# 특수기호를 쓸라면 %% // 두개 써야함 

# f 문자열 포매팅 개중요 ! // f를 써놓으면 바로바로 name age 같은 문자열을 쓸 수 있어서 용이하다고함. 
name = '홍길동'
age = 30
a = f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
print(a)

# 문자열 개수 세기 - count // h는 0번이라는걸 생각! 
a = "hobby"
print(a.find('b'))
# 없는걸 찾아달라고 하면 -1 이 나옴 
print(a.find('x'))

#반면에 find = index 같은 문법인데, index에게 없는걸 찾아달라고하면 오류가 발생.

# 문자열 삽입 - join
a = ",".join(['a', 'b', 'c', 'd'])
print(a)
# 콤마 뒤에 스페이스바 한번 하면 이래 나옴 차이를 이해
b = ", ".join(['a', 'b', 'c', 'd'])
print(b)
 
#소문자를 대문자로 바꾸기 - upper 
a = "hi"
print(a.upper())

# 대문자를 소문자로 바꾸기 - lower 
a = "HI"
print(a.lower())

# 왼쪽 오른쪽 공백 지우기 lstrip rstirp strip

# 문자열 바꾸기 - replace 
a = "Life is too short"
print(a.replace("Life", "your leg"))

# 문자열 나누기 - split 
a = "Life is too short" 
print(a.split())

b = "a:b:c:d"
print(b.split(':'))