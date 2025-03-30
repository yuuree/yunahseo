# 기본입출력
#입력받기
#a = input()
# print("내가 입력한 것:",a)
# b = input("입력해주세요.:")
# print(b)
# print("==========================")
#input으로 입력 받은 모든것은 str취급된다
from typing import get_overloads

#출력하기 다양한 방법
# last_name = "서"
# first_name = "윤아"
# name = last_name + first_name
#age = 27#int
#phone_number = "01085378870" 숫자는 맨앞에 0이 나올 수 없음
# print("hi"+"hellow"+"world")#문자열 더하기가 됩니다 hihellowworld
# print("hi","hellow","world")#.쉼표에 띄어쓰기가 포함되어 있다.hi hellow world
# print("제 전화번호는" "8537_8870" "입니다")제 전화번호는8537_8870입니다
#변수의 type을 알고싶을때 print(type())
# 윤아"

# print("제 나이는 {}입니다.".format(age))제 나이는 56입니다.옛날방식
# print("제 이름은 {}이고, 나이는{}입니다.".format(name,age))
# 제 이름은 서윤아이고, 나이는56입니다.
# print("제 이름은 {nm},나이는 {ag}입니다.".format(nm="서윤아",ag=56))
# 제 이름은 서윤아,나이는 56입니다.
# print("제 나이는 {age}입니다")#f_str방식 제 나이는 {age}입니다
# print("제 나이는 %s입니다.")#모든 문자를 문자열로 포맷팅해서 출력
# print("제 나이는 %d입니다.")#모든 숫자를 정수형으로 포맷팅해서 출력
# print("제 이름은 %s 이고, 제 나이는 %d 입니다." % (name, age))
# print("제 지분은 98% 입니다")
# print("%-10sHello" % "hi") 문자열 오른쪽 공백 10 hi        Hello
#print("%10s" % "hi")    hi 문자열 왼쪽 공백 10
# print("Eroor is %d%%." %  98)Eroor is 98%. %기호를 쓰려면 %를 두번 써야 된다
# print("%0.4f" % 3.42134234)#앞 0은 자리수를 의미. .4는 소수점 네번째 자리까지 표현
# print("%10.4f" % 3.42134234)#10은 자리수를 의미하므로 소수점4번째자리까지표현후남는자리만(4자리) 공백처리    3.4213
# 문자열(string), 문자1개(character), 정수(Integer),부동소수(floating_point) 8진수,16진수 literal %(문자 % 자체)
# name = input("이름: ")
# age  = input("나이: ")
# hobby =input("취미: ")
# adress = input("주소: ")
#
# print(f"제 이름은{"서윤아"}이고,제 나이는 {56}세 이며, 제 취미는{"요리"}이고,그리고 제 주소는{"양산시"} 입니다")
# 제 이름은서윤아이고,제 나이는 56세 이며, 제 취미는요리이고,그리고 제 주소는양산시 입니다
a = "Life is too short, yoo need python"
# print(a[3]) f
# print(a[-1])n
# print(a[-0])
# b = a[0] + a[1] + a[2] +a[3] Lif
# word = input("단어를 입력하세요:")
# print("첫번째 글자-",word[0])
# print("마지막 글자"),word[-1]
# print("===============")
# 첫번째 글자- p
# 마지막 글자
# ===============
# print(a[0:5])Life 끝번호는 포함하지 않는다
# print(a[5:8])is 슬라이싱은 원본에 영향을 주지 않음
# print(a[8:13])short
# print(a[::2])Lf ssotyone yhn
# print(a[::-1])nohtyp deen ooy,trohs si efiL문자열 뒤집기
# date1 ="3월17일"월일:3월17일
# date2 ="sunny"날씨:sunny
# print(input("월일:")) 3월17일
# print(input("날씨:")) sunny
# print(date1[:8]) 3월17일
# print(date2[:8])sunny

# print(len(a)) 문자열의 길이 34
# print(a.count("t"))특정문자가 몇개 있는지? 3
# print(a.index("t")) 특정문자의인덱스 찾기 8
# print(a.index("t",10,18)) "특정문자, 시작인덱스, 끝 인덱스" 인덱스== 문자열의 고유한 번호
# print(a.find("t"))
# print(a.find("t",10,18))*** find,index의 차이 find는 찾는 문자가 없으면 -1을 반환, index는 오류발생 find는 문자열(str)만 사용가능
# 인덱스는 문자열(str),리스트(list),튜플(tuple)만 가능

# print(",".join(["a","b","c","d"])) a,b,c,d  문자 합치기 사이에 콤바 추가
# print(a.upper()) LIFE IS TOO SHORT, YOO NEED PYTHON 대문자로
# print(a.lower()) life is too short, yoo need python 소문자로

# 컬렉션
# 리스트 생성
# fruits = ["apple", "banana", "cherry"]
# numbers = [1, 2, 3, 4, 5]
# mixed_list = ["안녕하세요", 42, 3.14, "python",100]
# 요소접근 (인덱싱)
# print(fruits[0])
# print(numbers[-1])
# fruits[1] = "blueberry" 요소변경
# print(fruits)
# fruits.append("grape") 리스트에 요소추가 2가지 dppend는 마지막에 요소추가
# fruits.insert(1,"mango")인서트는 특정위치에 추가
# print(fruits)
# fruits.remove("cherry")리무버는 특정값 삭제
# del fruits[0] 델은 특정 인덱스 삭제
# print(fruits)
# print(numbers[1:4])리스트 슬라이싱 가능
# print(numbers[::-1]) 리스트 슬라이싱 역순도 가능
# 튜플 생성
# colors =("red", "green"," blue")
# single_tuple =("hello",) 요소가 1개일때 꼭','를 붙여야 함
# print(colors[1]) green 요소접근
# print(colors[:2]) ('red', 'green') 튜플 슬라이싱  요소2는 제외한 나머지
# print(colors[::2]) ('red', ' blue') 튜플 슬라이싱 요소2를 제외한 나머지 역순
# print(colors[::-1]) (' blue', 'green', 'red')슬라이싱 역순

# items = (1. 2)
# print(items)
# a,b =(1, 2)
# print(a)
# print(b)
# a, _ = (1,2)
# print(a)
#
# a, b, *c,d = (1,2,3,4,5)
# print(a)
# print(b)
# print(c)
# print(d)
#

