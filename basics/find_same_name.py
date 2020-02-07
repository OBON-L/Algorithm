def find_same_name(data):
    length = len(data)
    same_name = []
    for i in range(length): # O(n**2)
        for j in range(i + 1, length):
            if data[i] == data[j]:
                same_name.append(data[i])
    return same_name

def find_same_name_using_set(data): 
    names = list(set(data)) # set함수는 값의 중복을 허용하지 않음 
    same_name = set([n for n in names if data.count(n) >= 2]) # O(n)
    return same_name
    
def main():
    names = list(input("사람들의 이름을 입력해주세요 : ").split())

    same_name = find_same_name(names)
    if same_name == []:
        print("입력하신 이름은 {}이며, 이 중에서 동명이인은 없습니다.".format(names, same_name))
    else:
        print("입력하신 이름은 {}이며, 이 중에서 동명이인은 {}입니다.".format(names, same_name))

main()
