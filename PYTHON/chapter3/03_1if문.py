# if문의 기본 구조
# true 
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
#false 
money = False
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# if 문의 구조 
# if 밑에는 참을 쓰는구조 else 밑에는 거짓을 쓰는구조
# if를 할라면 들여쓰기(tap) 구조도 알아야해~~

# 조건문 다음에 콜론(:) 이건 잊지말자 ! 꼭나온대
money = True 
if money:
    print("택시를")
    print("타고")
    print("가라")

# 비교 연산자 
# 등호를 쓰고 싶으면 비교 < >  이후 = <= / >= 이런식으로 

# 만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 가고, 그렇지 않으면 걸어가라. 
money = 2000
if money >= 3000:
    print("택시를 타고가라")
else: 
    print("걸어가라")

# 만약 3000원 이상 있거나 카드가 있다면, 택시를 타고 가고, 그렇지 않으면 걸어가라.
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# in / not in 
print(1 in [1, 2, 3])

print('j' not in 'python')

# in을 활용한 조건문 
pocket = ['papper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else: 
    print("그냥 가라")

# 조건문에서 아무 일도 하지 않게 설정하고 싶다면? pass 
pocket = ['papper', 'cellphone', 'money']
if 'money' in pocket:
    pass
else: 
    print("그냥 가라")

# 다양한 조건을 판단하는 elif 
# 주머니에 돈이 있으면 택시를 타고 가고, 주머니에 돈은 없지만 
# 카드가 있으면 택시를 타고 가고, 돈도 없고 카드도 없으면 걸어가라.
pocket = ['papper', 'cellphone']
card = True
if 'mpmey' in pocket:
    print("택시를 타고 가라")
else:
    if card: 
        print("택시를 타고 가라")
    else:
        print("걸어가라")

# 위를 줄여쓰기 위해서 elif 
# 가운데 else if 가 합쳐진다고 생각하면 좋음. 
pocket = ['papper', 'cellphone']
card = True
if 'mpmey' in pocket:
    print("택시를 타고 가라")
elif card: 
    print("택시를 타고 가라")
else:
    print("걸어가라")

# if 문을 한 줄로 작성하기 
# 예시
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

# 한줄로 패션코딩 무시해 
if 'money' in pocket: pass 
else: print("카드를 꺼내라")

