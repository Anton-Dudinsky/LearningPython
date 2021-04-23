def foo(h, sym):
    for i in range (0, h,1):
        for i in range(0,h,1):
            print(sym, end = '\t')
        print('\n')

sym = input()
h = int(input())
print(foo(h,sym))
