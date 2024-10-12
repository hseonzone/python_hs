odd = [1, 3, 5, 7, 9]
print(type(odd))

# 파이썬의 장점은 문자 숫자 상관없이 담을 수 있어. 
# 0, 1, 2 순서 생각 
a = [1, 2, 3] 
print(a[1])

# 0 1 2 / -3 -2 -1 생각! 
print(a[-1])

# 리스트 안에 리스트 뽑는법 
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[3])

# 중요함! 
print(a[3][1])

# 0이상 2미만 앞은 이상이고 뒤는 미만입니다 
a = [1, 2, 3, 4, 5] 
print(a[0:2])

# 2칸식 하고 싶을 때
print(a[::2])

#strint 문자열 (문자 + 리스트(배열))
#char 문자 

# 일반 숫자 더하기 문자는 불가능해 str 로 감싸줘야함.
a = [1, 2, 3]
print(str(3) + "hi")

# 리스트의 값 수정하기 
a = [1, 2, 3] 
a[2] = 4 
print(a)

# del 함수를 사용해 리스트 요소 삭제하기 
a = [1, 2, 3, 4, 5] 
del a[1]
print(a)

del a[2:]
print(a)

# 리스트에 요소 추가하기 
a = [1, 2, 3] 
a.append(4)
print(a)

# 리스트에 리스트 
a.append([5,6,7])
print(a)

# 리스트 정렬 - sort 
a = [1, 4, 3, 2] 
a.sort()
print(a)

b = ['c', 'd' ,'e', 'f']
b.sort()
print(b)

# 리스트 역 정렬 - reverse
a = ['a' , 'c', 'b']
a.reverse()
print(a)

# 내림차순을 하고 싶으면 정렬 하고 해야지 잘 생각.~
a = ['a' , 'c', 'b']
a.sort()
a.reverse()
print(a)

# 인덱스 함수는 위치값을 리턴한다. 
a = [1, 2, 3,] 
print(a.index(3))

# 리스트 요소에 삽입 - insert 0번째에 4를 추가할 것이다.
a = [1, 2, 3] 
a.insert(0, 4)
print(a)

# 리스트 요소 제거 - remove 

# 리스트 요소 끄집어 내기 - pop // 날려버리는 개념임 remove랑 비슷해.
a = [1, 2, 3] 
a.pop(1) 
print(a)

# 리스트 요소 개수 세기 - count 

# 리스트 확장 - expend / append 와 차이는 얘는 [] 를 가져옴.