def f(x):
    return x**3 - x - 2

a = 1.0
b= 2.0
eps = 0.0001

while abs(b-a)>eps:
    c=(a+b)/2.0
    if f(a)*f(c)<=0:
        b=c
    else:
        a=c

qwe = (a+b)/2.0
print(f"Корень: ",qwe)