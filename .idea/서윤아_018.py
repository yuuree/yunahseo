#a=  "life is too long, you need python"
# print(a[0].isupper())#a 문자열의 첫번째 글자는 대문자입니까?
# print(a[8].lower())#a 문자열의 8번째 인덱스의 소문자는 무엇입니까?
# print(a.strip())#문자열 바깥 양쪽 공백을 제거합니다.
# print(a.rstrip())#문자열 바깥 오른쪽 공백을 제거합니다.
# print(a.lstrip())#문자열 바깥 왼쪽공백을 제거합니다.
# print(a.replace(",", ""))#안쪽공백을 지우고 싶을때는 repalace함수를 쓴다
# print(a.split())# 탭(tab).공백, 쉼표로 나누는 함수 리스트 형태로 나눠짐
#
#b="a:b:c:d"
#print(b.split(":"))#":"기준으로 나눠짐 리스트형태

#컬렉션(여러개의 데이터를 저장하고  관리하는 자료구조:리스트,튜플,딕셔너리,세트가 있다.
#각 컬렉션들의 특징
#리스트:순서가 있고 중복이 가능하고 요소추가/삭제가 가능 [ ](대괄호형태)
#튜 플:순서가 있고 중복이 가능하고 요소추가/삭제가 안된다:변경안되나,카운터,인텍싱,슬라이싱,언패킹가능
# 왜? 원본의 가공이 있지만 원본은 변하지 않으니까 ():소괄호 형태
#리스트와 튜플의 다른점: [1]는 하나의 요소가능하나 튜플은 요소가 하나만 들어갈때 쉼표 a=("first",)
#딕셔너리:키_값 쌍으로 데이터를 저장하는 자료형,키는 고유해야하며(중복안됨),키를 사용해 빠르게 접근
#{}-중괄호형태, key_value 각 키와 값은 콜론:으로 구분,쌍은 쉼표로 구분
#세트:인덱스가 없는 구조로 연산(*집합연산을 얘기)을 하기위해 지원하는 자료구조 ,교집합,합집합,차집합
#세트는 순서가 없고 중복된 값을 허용하지 않음 숫자뿐만 아니라 문자열 논리값 등 다양한데이터 저장 가능
#{}-중괄호형태 중괄호안에 내용들을 ,(쉼표)로 구분 서로다른 값들을 모아서 관리하는데 적합
# 리스트 예제 및 문제
#fruits  = ["orange", "apple", "banana"]
# numbers = [1, 3, 4, 5,"hi"]
# bools   = [True, False,True]
#mixed_list = ["안녕하세요",12 , True] mixed 리스트에서 ctrl+spaebar를 누르면 쓸수 있는 함수목록을 보여준다
#
# print(fruits)
# print(fruits[2][1])
# print(fruits [2])
# fruits [1] = "cherry"# 리스트 안 요소변경
# print(fruits)
# numbers.append("hi")
# print(numbers)
# numbers.insert(1,2)
# print(numbers)
# print(numbers.pop())#리스트의 마지막 코드가 리턴된다.

#numbers = [1, 3, 4, 5 ]
# numbers.remove("hi")#리스트 안의 특정요소를 제거
# mixed_list = ["안녕하세요", 12 , True]
# print(len(mixed_list))# 리스트의 인덱스 길이
# numbers = [1, 3, 5, 6 ]
# numbers.sort()#작은순대로 정렬
#
# fruits  = ["cherry", "apple", "banana"]
# fruits.sort()
# print(fruits)#문자, 숫자 정렬 가능
# bools = [False, True, True]
# bools.sort()
# print(bools)#f=0, t=1
# numbers=[1, 3, 5, 6]
#numbers.sort(reverse=False)
#print(numbers)#reverse=false는 작은 순 #sort()작은순 옵션 reverse=ture는 큰순
# numbers.reverse()
# print(numbers)#그냥 reverse를 입력했을때 리스트 목록의 역순으로 출력

# fruits = "apple","orange","banana"
# fruits="_".join(fruits)
# print(fruits)
#리스트 문제
# cart=[]
# cart.append(input("추가할 상품"))
# cart.append(input("추가할 상품"))
# cart.append(input("추가할 상품"))
# print(cart)#리스트에 추가
#튜플의 형태
#colors  = ("red","green","black")
#numbers = (1, 5, 3, 9)
#bools   = (True, False, True)
#mixed_tuple = ("red", 1, True)
#a=("first",)#요소가 하나만 들어갈때 쉼표를 찍어줘야 함(단, 리스는 하나의 요소도 가능)
#print(colors[1])#요소접근은 리스트와 같음
#colors[1]="yellow" # 튜플은 변경 안됨
#print(numbers[0:2])#슬라이싱 가능
#print(numbers.count(1))
#print(numbers.index(3))#요소3의 인덱스번호는 2
#a,b,c=colors
# print(a,b,c) #소괄호가 벗겨져 나옴
# print(c)#특정요소 출력
#딕셔너리 예제



















