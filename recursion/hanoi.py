# 단순히 총 이동 횟수만을 구하는 함수
def hanoi_count(n):
    if n == 1: return 1
    return 1 + 2 * hanoi_count(n - 1)

# 과정 설명을 위한 함수
def hanoi(n, fr, to, th): 
    if n == 1 : # 종료 조건 
        print("{}에서 {}로 원반을 이동시켰습니다.".format(fr, to))
        return
    hanoi(n - 1, fr, th, to)
    hanoi(1, fr, to, th) # print("{}에서 {}로 원반을 이동시켰습니다.".format(fr, to)) 로 대체 가능 
    hanoi(n - 1, th, to, fr)

# 하노이의 탑 알고리즘의 시간 복잡도 : O(2**n)
    
def main():
    n = int(input("원반의 개수를 입력해주세요 : "))
    hanoi(n, *(input("처음 원반을 놓을 기둥, 목적지 기둥, 그 외의 기둥 순서대로 입력해주세요 : ").split())) # unpacking

main()
