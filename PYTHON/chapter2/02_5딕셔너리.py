# 딕셔너리
dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(type(dic))

# 딕셔너리 쌍 추가하기 key / value 개념임 
a = {1: 'a'}
a[2] = 'b'
print(a)

a = {1: 'a', 2: 'b', 'name' : 'pey', 3: [1, 2, 3]}
del a['name']
print(a)

grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])

# 실전용 
dic = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
print(dic['name'])

# 딕셔너리 만들 때 주의할 사항. 

# key는 무조건 한개여야해 , 이런 경후 뒤에거가 덮어버림 1개로 
a = {1: 'a', 1:'b'}
print(a)

# key가 변형 가능한 자료이기 떄문에, [1.2] 이런건 불가능해
#a = {[1,2] : 'hi'}

# 딕셔너리 관련 함수 

a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.keys())

# 반복문에선? 나중에 다시 개념함. 
for k in a.keys():
    print(k)

# valuse 리스트 만들기 
print(a.values())

# key, valuse 다 뽑으려면, items 함수를 사용하면 가능해. 
print(a.items)

# key, value 모든걸 다 지우려면, 
a.clear() 
print(a)

# key로 value 얻기 - get 함수 
# 이놈은 주로 none 이라는 답을 얻고 싶을 때 사용하는 듯. 
# 그냥 print (asdf) 없는 걸 물으면, 오류발생하는데, 
# get을 이용하면, none 이라는 결과값이 나옴 
print(a.get('asdf'))

# 해당 딕셔너리에 있는지 없는지 체크 - in 
print('name' in a)

