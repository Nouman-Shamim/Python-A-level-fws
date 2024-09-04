def foo(x,y):
    if x<y:
        return foo(x+1,y-2)
    elif x==y:
        return 2*foo(x+2,y-3)-3
    else:
        return 2*x+3*y

print(foo(3,12))
