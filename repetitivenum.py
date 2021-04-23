def foo(number, numer):
    count = 0
    s = [int(i) for i in str(number)]
    for i in s:
        if s[i] == numer:
            count += 1
    return count

n = input()
num = int(input())
print(foo(n, num))
