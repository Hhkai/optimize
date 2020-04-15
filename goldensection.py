# coding:utf-8

def f(x):
    return x*x+4*x+5

def Dichotomous(f, a, b, delta):
    eps = 0.001
    iter = 1
    while b - a > delta:
        # 取中点
        print(iter, a,b)
        iter += 1
        mid = 0.5 * (a + b)
        lamb = mid - eps
        mu = mid + eps
        # 差分近似导数
        flamb = f(lamb)
        fmu = f(mu)
        if flamb < fmu:
            b = mu 
        else:
            a = lamb
        print(lamb,mu,flamb, fmu)
        print('---------')
    print(a,b)
#
#Dichotomous(f, -10, 10, 0.1)
def GoldenSection(f, a, b, delta):
    alpha = 0.618
    iter = 1
    lamb = a + (b-a)*(1-alpha)
    mu = a + (b-a)*alpha 
    flamb = f(lamb)
    fmu = f(mu)
    while b-a>delta:
        print("<tr><td align=center>%d</td>\n<td align=center>%.6f</td>\n<td align=center>%.6f</td>\n<td align=center>%.6f</td>\n<td align=center>%.6f</td>\n<td align=center>%.6f</td>\n<td align=center>%.6f</td>\n</tr>" % (iter, a,b,lamb,mu,flamb,fmu))
        iter += 1
        
        if flamb > fmu:
            a = lamb 
            lamb = mu 
            mu = a + (b-a)*alpha 
            flamb = fmu 
            fmu = f(mu)
        else : 
            b = mu 
            mu = lamb 
            lamb = a + (b-a)*(1-alpha)
            fmu = flamb
            flamb = f(lamb)
    print(a,b)
#
#GoldenSection(f, -10, 10, 0.1)
def Fibonacci(f, a, b, delta):
    F=[1,2]
    a1 = 1
    a2 = 2
    n = (b-a) / delta 
    ind = 1
    while True:
        c = a1 + a2 
        F.append(c)
        ind += 1
        a1 = a2 
        a2 = c
        if c > n:
            break
    iter = 1
    lamb = a + (b-a)*(F[ind - 2] / F[ind])
    mu = a + (b-a)*(F[ind - 1] / F[ind])
    flamb = f(lamb)
    fmu = f(mu)
    while ind>1:
        print("<tr><td align=center>%d</td>\n<td align=center>%.6f</td>\n<td align=center>%.6f</td>\n<td align=center>%.6f</td>\n<td align=center>%.6f</td>\n<td align=center>%.6f</td>\n<td align=center>%.6f</td>\n</tr>" % (iter, a,b,lamb,mu,flamb,fmu))
        iter += 1
        ind -= 1
        if flamb > fmu:
            a = lamb 
            lamb = mu 
            mu = a + (b-a)*(F[ind - 1] / F[ind])
            flamb = fmu 
            fmu = f(mu)
        else : 
            b = mu 
            mu = lamb 
            lamb = a + (b-a)*(F[ind - 2] / F[ind])
            fmu = flamb
            flamb = f(lamb)
    print(a,b)
#
#Fibonacci(f, -10, 10, 0.1)
def f_dash(x):
    return x*2 + 4
def bi_diff(f, f_dash, a, b, delta):
    lamb = a+(b-a) * 0.5
    fdash_lamb = f_dash(lamb)
    iter = 1
    while b-a > delta:
        print("<tr><td align=center>%d</td>\n<td align=center>%.6f</td>\n<td align=center>%.6f</td>\n<td align=center>%.6f</td>\n<td align=center>%.6f</td></tr>" % (iter, a,b,lamb, fdash_lamb))
        iter += 1
        if fdash_lamb == 0:
            break
        if fdash_lamb > 0:
            b = lamb
        else:
            a = lamb
        lamb = a+(b-a) * 0.5
        fdash_lamb = f_dash(lamb)
    print(a,b)
        
bi_diff(f, f_dash, -10, 10, 0.1)