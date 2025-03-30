# items = (1, 2) 튜플의 unpacking
# print(items)
# a,b =(1, 2)
# print(a)
# print(b)
# a, _ = (1,2) 사용되지 않거나 필요없는 변수는 언더스코어_, *표시를 함
# print(a)
#
# a, b, *c,d = (1,2,3,4,5) 변수명 앞에 *표시를 하면 여러개 값을 갖는 리스트가 됩니다.
# print(a) a는 1이 할당
# print(b) b는 2가 할당
# print(c) 나머지  값 할당
# print(d) d는 5가 할당
# (1, 2)
# 1
# 2
# 1
# 1
# 2
# [3, 4]
# 5
# 딕셔너리
# profile = {
#      "name": "서윤아",
#      "나이": 56,
#      "취미":["요리", "수영"],
#      }
# print(profile["name"])
# print(profile["취미"][1])
# profile["나이"] = 56
# print(profile)
# profile["직업"] = "공인회계사"
# print(profile)
# #del profile["직업"]
# print(profile)
# profile.clear()
# #print(profile)
#
# print(profile.keys())
# key_list = list(profile.keys())
# key_list.append("전화번호")
# print(key_list)
#
# print(profile.values())
# value_list = list(profile.values())
# value_list.append("1234")
# 서윤아
# 수영
# {'name': '서윤아', '나이': 56, '취미': ['요리', '수영']}
# {'name': '서윤아', '나이': 56, '취미': ['요리', '수영'], '직업': '공인회계사'}
# {'name': '서윤아', '나이': 56, '취미': ['요리', '수영'], '직업': '공인회계사'}
# dict_keys([])
# ['전화번호']
# dict_values([])
# item_list = list(profile.items())
# item_list.append(("직업", "free_lenser")) #튜플형식으로 리스트 반환
# print(item_list)
# [('name', '서윤아'), ('나이', 56), ('취미', ['요리', '수영']), ('직업', 'free_lenser')]


# Python_grade = {
#     "kelly": "B",
#     "json": "A",
#     "ian": "C",
#     "elly":  "D",
# }
item_list = list(Python_grade.items())

# print(sorted(Python_grade.items())) #키기준 오름차순 정렬
# print(sorted(Python_grade.items(),reverse=True))#키기준 내림차순 정렬
# [('elly', 'D'), ('ian', 'C'), ('json', 'A'), ('kelly', 'B')]
# [('kelly', 'B'), ('json', 'A'), ('ian', 'C'), ('elly', 'D')]

# print(sorted(Python_grade.items(),key=lambda x: x[1])) 값기준 오름차순
# print(sorted(Python_grade.items(),key=lambda x: x[1], reverse=True))값 기준 내림차순
# [('json', 'A'), ('kelly', 'B'), ('ian', 'C'), ('elly', 'D')]
# [('elly', 'D'), ('ian', 'C'), ('kelly', 'B'), ('json', 'A')]

# student ={}
# name =  input("학생이름을 입력하세요:")
# score = int(input(f"{name}의 점수를 입력하세요:"))
# student[name] = score
# print(student)
# 학생이름을 입력하세요: 성수현
#  성수현의 점수를 입력하세요:95
# {' 성수현': 95}

#세트
# fruties = {"사과", "바나나","오렌지"}
# print(fruties)
# string_set =set("hello")
# print(string_set)
# nums = {1,2,2,3,3,3,4}
# print(nums)
# num_list = [1,2,3,3,4,4]
# list_set =set(num_list)
# print(list_set)
# empty_set = set()

s = {1,2,3,}
# s.add(4)
# print(s)
# {1, 2, 3, 4}
s.update([5,6,7])
# print(s)
# {1, 2, 3, 5, 6, 7}
#s.remove(3) KeyError: 10 존재하지 않는 값 오류발생
#s.discard(10)오류없음
#print(s)
# x = 10
# y = 20
# z = 30
# # x+= 10 대입연산자
# x-=  5
# x*=  3
# x//= 2 나누고 몫이 실수
# x/=  2 나누고 몫이 정수
# print(x) 11.0
# 비교연산자
# print(x == z)
# print(x <  y)
# print(x == y)
# print(x != y)
# print(x <= y)
# print(x >= z)
# False
# True
# False
# True
# True
# False

# a = True
# b = False
# print(not a and b)
# print(a or b)
# print(not a)
#
# False
# True
# False

# a = 10
# b = 20
# max_value = a if a > b else b
# print(max_value) 20

# score = 85
# grade = "A" if score >=90 else("B" if score >=80 else "c")
# print(grade) B

# num = 7
# result ="짝수" if num %2 == 0 else "홀수"
# print(result)홀수

