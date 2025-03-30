# import requests
#
# response =requests.get("https://www.naver.com/")
#
# print(response.status_code)
# print(response.text)
from ctypes.macholib.dyld import DEFAULT_LIBRARY_FALLBACK
from operator import truediv

import pandas as pd
from numpy.ma.core import filled

#
# print(df)
# print(df.describe())# 요약 분석
"""
count - 해당 열의 데이터 갯수
mean-평균값
std-표준편차(데이터의 분산정도)
min-최소값
25%-데이터의 25%지점
50%-"
75%-"
max-최대값
"""
# print(df[["Age","Salary"]])

# import matplotlib.pyplot as plt


# plt.show()

# import numpy as

# arr1 = np.array([1,2,3,4,5])
# print(arr1)
#
# arr2 = np.array([[1,2,3],[4,5,6]])
# print(arr2)
#
# zeros = np.zeros((3,4))#0으로 채운 다차원배열
# print(zeros)
#
# # 1로 채운 다차원 배열
# ones = np.ones((3,4))
# print(ones)

# 특정한 값으로 채운 다차원 배열

# filled = np.full((3,4),5)
# print(filled)

# 연속된 값으로 채운 일차원 배열
# arr =np.arange(1,10,2)
# print(arr)
# 랜덤 값으로 채운 일차원 배열
# random_arr = np.random.randint(1,100,(3,4))
# print(random_arr)

# arr1 = np.array([1,3,5])
# arr2 = np.array([2,5,8])
#
# print(arr1 + arr2)
# print(arr1 - arr2)
# print(arr1 * arr2)
# print(arr1 / arr2)

# import seaborn as sns
#
# df = pd.read_csv("tips.csv")
# plt.figure(figsize=(8,5))
# sns.scatterplot(x="total_bill",y="tip",hue="sex",data=df,palette="Set2")
# plt.xlabel("Total Bill ($)")
# plt.ylabel("Tip ($)")
# plt.show()
# import requests
# response = requests.get("https://knitshare.link")
# print(response.status_code)
# print(response.content)
#
# import pandas as pandas
# df = pd.png("color.chart")
# print(df)
# print(df.describe())

# import random
# # use_number = 1
# # guess_number =int(input(f"숫자를입력하세요:"))
# # correct_number=[1,2,3,4,5,6,7,8]
# # while guess_number < 8:
# #    print("숫자:")
# #    guess_number += 1
# #    "continue"
# # else: guess_number == 8
# # print(f"게임종료!!")
#
#
#
# import random
# computer_score = 0
# use_score = 0
# name =["A","B","C"]
# add_incentive = ["여행떠나기", "하루만 놀기","게임머니획득"]
#
# def introduce(self):
#     int(input(f"{self.name},{use_score}을 입력하세요"))
#     while True:
#
#         if use_score <= 70:
#             continue
#         elif use_score >=80:
#             print(f"add_incentive[2]를 획득할 수 있습니다")
#             continue
#         elif use_score <=90:
#             print(f"add_incentive[1]할 수 있습니다")
#             continue
#         elif use_score <=95:
#             print(f"add_incentive[0]할 수 있습니다")
#             continue
#         elif use_score != "exit":
#             input(f"종료하려면 exit 입력하세요: ")
#         else: use_score == 100
#         "break"

# class Car:
#     pass
# a = 10
# if a < 100:
#     pass

