# 튜플이 리스트랑 다른점은, 변경이 안돼.

#리스트 쓰는 방식 []
a = [1, 2, 3]

#튜플 쓰는 방식 ()
t1 = ()
print(type(t1))

# 튜플인걸 알려주기 위해서 콤마가 있어야함
t2 = (1,)
print(t2)

# 리스트랑 특성이 비슷하게 튜플 안에 튜플을 넣을 수 있음.
t5 = ('a', 'b', ('ab', 'cd'))
print(t5)

# 튜플 값을 지우기 위해선?  오류가남. 
t1 = (1, 2, 'a', 'b')
# del t1[0]

# 슬라이싱 하기, 
print(t1[1:])
# 변하지 않아 슬라이싱해도, 잠깐 임시로 쓴 느낌. 
print(t1)

# 튜플은 더하기 곱하기 다 가능해. 
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t3 = t1 + t2
print(t3)
