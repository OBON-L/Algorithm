def factorial_using_recursion(n): #O(n)
    if 0 <= n <= 1:
        return 1
    return n * factorial_using_recursion(n - 1)

def factorial_not_using_recursion(n): #O(n)
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    n1 = int(input("수를 입력해주세요 : "))
    print("{}! = {}".format(n1, factorial_using_recursion(n1)))
    
    n2 = int(input("수를 입력해주세요 : "))
    print("{}! = {}".format(n2, factorial_using_recursion(n2)))

main()
