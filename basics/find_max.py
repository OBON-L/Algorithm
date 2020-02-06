def find_max(data):
    max = data[0]
    for i in range(1, len(data)):
        if max < data[i]:
            max = data[i]
            max_index = i
    return max, max_index #packing

def main():
    lst =  list(map(int, input("리스트에 넣을 데이터를 입력해주세요\n").split()))
    print("입력된 리스트의 값 : {}\n".format(lst))
    
    tpl =  tuple(map(int, tuple(input("튜플에 넣을 데이터를 입력해주세요\n").split())))
    print("입력된 튜플의 값 : {}\n".format(tpl))

    print("lst의 최댓값은 %d이며, 최댓값의 index는 %d입니다." % (find_max(lst)))
    print("tpl의 최댓값은 {}이며, 최댓값의 index는 {}입니다.".format(*(find_max(tpl)))) # unpacking

        
main()
