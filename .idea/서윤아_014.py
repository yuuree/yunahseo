#name = "서윤아"
#age= 56.15
# print("제 이름은" + name +"입니다.") #문자열 플러스는 뛰어쓰기가 안됨
# print("제 이름은", name ,"입니다.") #표는 띄어쓰기가 포함
# print("제 나이는 ", age ,"입니다") # age라는 변수선언 #문자열은 쌍따옴표로 감싸여있어야함
#  #정수+문자열은 안됨 쉼표는 띄어쓰기가 포함되어 있고 변수명이 있는 공간일 뿐이므로 있고 없고의 차이
# print("제 나이는 {} 입니다.".format(age))#format은 중괄호 안에 들어갈 변수명
#  print("제 나이는 {a} 이고 이름은 {b} 입니다.").format(a="56", b="서윤아")#즉석으로 직접 변수를 만들때
# print(f"제 나이는 {age} 이고 이름은 {name} 입니다.")#f_string
# print(f"제 나이는 %s 입니다." %age)#문자열로 들어간다
# print(f"제 나이는 %d 입니다."%age)#모든 숫자를 정수로 바꿔서 취환 문자열은 정수로 바꿀수 있지만 정수는 문자열로 바꿀 수 없다
# print(f"제 나이는 %d 이고 이름은 %s입니다." %(age, name) )
# print("제 지분은 %d%% 입니다." % 2 )# %를 문자열로 할때는 %%로 한다.
#from curses.ascii import isupper

# print("%10.2f" %3.141565) #0은 자리수를 의미 스페이스 공백이 생긴다 점도 자리수에 포함
#%"자릿수". "몇번재 소수점"f 10자리 .2는 소수점 둘째자리까지

#input()이라는 함수

#input()

# email=input("이메일:")
# hobby=input("취미:")
# age=int(float(input("나이:")))
#
# print(f"제 이메일은{email}이고, 취미는{hobby}이며,나이는{age}입니다")

a= "life is too short, you need python"

#print(a[2:10:2])

# date = "20250218sunny"
# date2 ="20260505cloudy"
#
# print(f"연도는{date2[0:4]},월은 {date2[4:6]},일은 {date2[6:8]},날씨는 {date2[8:]}")

# print(a.rstrip())
# print(a.replace("",""))

# print(a.split(":"))
b= "a:b:c:d"
print(b.split(":"))




