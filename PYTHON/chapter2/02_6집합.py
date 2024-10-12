# 집합 자료형 
s1 = set([1, 2, 3])
print(s1)

# 집합 문자열 순서 x 중복 재거 / 수학 집합을 생각! 
s2 = set("hello")
print(s2)

# 교 / 합 / 차 
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합 구하기 
print(s1 & s2)

# 합집합 구하기 (shift + \)
print(s1 | s2)

# 차집합 구하기 
print(s1 - s2)

# 집합 자료형 관련 함수 

# 값 1개 추가하기 - add 
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

# 값 2개 추가하기 - update 
s1 = set([1, 2, 3])
s1.update([4,5,6,])
print(s2)

# 특정 값 제거하기 - Remove 
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)

# 언제 정말 활요하냐? / 리스트를 집합으로 만든 과정 그럼 중복이 다 제거가 돼
li = [1,2,2,2,2,3,3,3,3,3,4]
s1 = set(li)
print(s1)