# 변수 이래도 가능, 
a, b = ('rt' , 'qwer')
print(a)
print(b)

# 리스트 
[a, b] = ('rt' , 'qwer')
print(a)
print(b)

# 한줄 
a = b = 'rt' 
print(a)
print(b)

# 실 활용 많음 / a와 b의 값을 바꾸려면 
a = 3 
b = 5 
a,b = b,a
print(a)
print(b)