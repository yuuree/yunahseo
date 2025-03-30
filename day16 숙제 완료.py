try:
    my_dict = {1: "사과", 2: "바나나", 3: "딸기", 4: "포도", 5: "수박"}
    result = my_dict[int(input("숫자를 입력 : "))]
except KeyError:
    print("해당 키는 존재하지 않습니다.")
except ValueError:
    print("숫자를 입력해주세요.")
else:
    print(result)
finally:
    print("완료")