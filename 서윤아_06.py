# a = 10
# b = 20
# def plus(a,b):
#     return a+b
# result = plus(10,20)
# print(result)

# name = {}
# def hello(name):
#     print(f"안녕하세요,{name}입니다.")
# hello("서윤아")
# 안녕하세요,서윤아입니다.

# a = ()
# b = ()
# def plus(a,b):
#     print(a + b)
# plus( 45, 134)
# plus(224, 325)
# plus(5,9)

# name = "강호동"
# age =  46
# def introduce(name, age):
#     print(f"제 이름은 {name}이고 나이는 {age}입니다")
# introduce(name, age)

# multiple_seven = ()
# def multiple_seven(num):
#     return num*7
# print(multiple_seven(4)) 28
# result =multiple_seven(7)49
# print(result)
# divide_seven =()
# def check_divide_seven(num):
#     if num%7 ==0:
#         return True
#     else:
#         return False
# print(check_divide_seven(7)) True
# print(check_divide_seven(18))False
# print(check_divide_seven(49))True
# def factorial(num):
#     sum = 1
#     for n in range(num):
#      print(f"n:{n}")
#     sum = sum *(n+1)
#     print(f"sum:{sum}")
# print(factorial(7))
# n:0
# n:1
# n:2
# n:3
# n:4
# n:5
# n:6
# sum:7
# None

# def cal_everage(scores):
#     sum = 0
#     for score in scores:
#         sum+=score
#     average = sum/len(scores)
#     return average
# score_list_1 =[55,70,100]
# score_list_2 =[100,99,88]
# score_list_3 =[80,70,60]
#
# print(cal_everage(score_list_1))
# print(cal_everage(score_list_2))
# print(cal_everage(score_list_3))
# 75.0
# 95.66666666666667
# 70.0

#콜백함수
# 함수를 매개변수로 전달하여 필요할 때 호출하도록 하는 개념
# 어떤 함수가 실행되는 동안 미리 정의된 다른 함수를 호출하여 실행하는 역활

# def calculater(x,y,operation):
#     return operation(x, y)
# def plus(x, y):
#     return x+y
# def minus(x, y):
#     return x-y
# def multiple(x,y):
#     return x*y
# def divide(x, y):
#     return x/ y
# plus_result = calculater(4,5,plus)
# minus_result= calculater(4,5,minus)
# multiple_result=calculater(4,5,multiple)
# divide_result=calculater(4,5,divide)
#
# print(plus_result)
# print(minus_result)
# print(multiple_result)
# print(divide_result)
#
# 9
# -1
# 20
# 0.8

#import time

# def timer(pause_second,callback):
#     print("타이머가 시작됩니다.")
#     print(pause_second,"몇 초 뒤에 요청하신 함수가 호출됩니다")
#
#     #time_sleep(pause_second)
#     callback()
#     print("타이머가 종료됩니다.")
# def hello():
#     print("hello world")
#     timer(5, hello)
#람다함수(익명함수)
#특정범위내에서만 사용되거나 호출되는 횟수가 한번인 경우에 매우 유용
#lambda 매개변수 1,매개변수2,---함수내부코드
# def add(x, y):
#     return x+y
# print(add(3,5))
# add_lamda = lambda  x,y:x+y
# print(add_lamda(3,5))
# numbers =[1,2,3,4,5]
# squared =list(map(lambda x:x**2,numbers))모든요소를 지공
# print(squared)
# [1, 4, 9, 16, 25]

# numbers =[1,2,3,4,5,6,7,8,9,10]
# even_numbers =list(filter(lambda x:x%2==0,numbers))짝수만 필터링
# print(even_numbers)
# [2, 4, 6, 8, 10]
# parity =lambda x:"짝수" if x %2==0 else "홀수"
# print(parity(5))
# 홀수

# add_lambda =lambda a,b:a+b
# print(add_lambda(56,78)) 134

# x =int(input("숫자a:"))
# y =int(input("숫자b:"))
# def add(x,y):
#     return x+y
# print(add(x,y))

# def is_even(n):
#     return n%2 ==0
# print(is_even(4))True
# print(is_even(7))False
# print(is_even(10))True


# import math
# print(math.ceil(3.14))#올림 4
#copysign-두번째 인자의 부호만 취해 첫번째 인자에 적용
#print(math.copy sign(3.14, -1)) -3.14
#fabs-절대값을 반환하는 매서드
# print(math.fabs(-3.14))3.14
#fatorial- 팩토리얼을 구하는 메소드
#print(math.factorial(7))
#floor-내림
#print(math.floor(-3.14))#-4 무조건 아래로 내림
#print(math.trunc(-3.14))#-30 0을 향해서 내림
#log(a,b)b를 밑으로 하는 log a에 대한 로그값
#print(math.log(10,10))#1.0
#print(math.pi)3.141592653589793
#난수
import random
# print(random.randint(1, 10))
# print(random.randrange(1,10,2))
# #shuffle
#abc =["a","b","c","d","e"]
# random.shuffle(abc)
# print(abc)['b', 'd', 'c', 'e', 'a']
#choice
# abc =["a","b","c","d","e"]
# print(random.choice(abc))
# menu = "삼겹살","된장찌개","맥주","소주"
# print(random.choice(menu))
#현재 날짜
# from datetime import datetime,timedelta
#
# now = datetime.now()
# print(now)
#
# one_week_later = now +timedelta(days=7)
# print(one_week_later)
#
# formatted_date =now.utctime("%Y%m%d %H:%M:%S")
# print(formatted_date)

# import os
#
# print(os.getcwdu())# 현재 디렉토리
# print(os.listdir())#현재 폴더의 목록
#
# if not os.path.exists("new_folder"):
#     os.mkdir("new_folder")

# import re
#
# pattern = "[a-zA-Z0-9._+-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}"
# email ="dongyoon7212@naver.com"
# if re.match(pattern,email):
#      print("올바른 이메일")
# else:
#      print("틀린 이메일")
#
# pattern = r"\d{3}-\d{4}-\d{4}"
# phone_number ="010-1234-5678"
#
# if re.match(pattern,phone_number):
#      print("올바른 전화번호")
# else:
#      print("틀린 전화번호")











