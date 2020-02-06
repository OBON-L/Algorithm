import timeit

def get_sum1(n): # O(n)
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum

def get_sum2(n): # O(1)
    return n * (n + 1) // 2

def cal_time(func, d):
    n = int(input("숫자를 입력해주세요 : ")) # 5,000,000
    start = timeit.default_timer()
    print("{}까지의 합은 {}입니다.".format(n, func(n)))
    stop = timeit.default_timer()
    print("get_sum{} 함수를 실행하는데 걸린 시간 : {}".format(d, stop - start))
    print("----------------------------------------------")
    return stop-start
    
def main():
    t1 = cal_time(get_sum1, 1)
    t2 = cal_time(get_sum2, 2)

    if(t1 > t2):
        print("get_sum{} 함수가 get_sum{} 함수보다 {}초 빨랐습니다.".format(2, 1, t1 - t2))
    else:
        print("get_sum{} 함수가 get_sum{} 함수보다 {}초 빨랐습니다.".format(1, 2 , t2 - t1))
        
    # get_sum2 함수가 get_sum1 함수보다 0.8051861999999996초 빨랐습니다.
    
main()
