def foo(l):
    temp = l[len(l)-1]
    for i in range(len(l)-2, -1, -1):
        l[i+1] = l[i]
    l[0] = temp
    print(l)

l = [ int(i) for i in input().split()]
foo(l)
