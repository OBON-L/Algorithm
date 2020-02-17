from collections import defaultdict

def find_same_name_sd(data): #setdefault을 사용한 함수 - O(n)
    names = dict()

    for n in data:
        names[n] = names.setdefault(n, 0) + 1 #딕셔너리의 메소드 setdefault

    overlap_n = {n for n in names if names[n] >= 2} #set comprehension

    return overlap_n

def find_same_name_dd(data): #defaultdict을 사용한 함수: collections 모듈을 import 해줘야 함 - O(n)
    names = defaultdict(int) #defaultdict함수를 호출하면서 int 함수 등록: int 함수는 아무 값도 인자로 전달받지 않으면 0을 반환 
    
    for n in data:
        names[n] += 1

    overlap_n = {n for n in names if names[n] >= 2} #set comprehension

    return overlap_n
    

def main():
    names = list(input("여러 명의 이름을 입력해주세요: ").split())
    print("입력하신 사항은 다음과 같습니다\n {}\n".format(names))
    print("setdefault를 이용해 발견한 동명이인의 이름은 {}입니다\n".format(find_same_name_sd(names)))
    print("defaultdict를 이용해 발견한 동명이인의 이름은 {}입니다\n".format(find_same_name_dd(names)))

main()
