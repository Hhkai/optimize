# input: A, b, x(0), d(1)

# min f(x) = 1/2 * x^T * A * x + b^T * x + c

import numpy as np

def diyidaoti(x):
    return (8*x[0]-4*x[1],8*x[1]-4*x[0]-12)

def dierdaoti(x):
    return (2*x[0]-2*x[1]-x[2]+1,-2*x[0]+4*x[1]+3,2*x[2]-x[0]-1)

    
def fun_grad(x):
    # return np.array(diyidaoti(x))
    return np.array(dierdaoti(x))
# A = [
    # [8, -4],
    # [-4, 8]
    # ]
A = [
    [2, -2, -1],
    [-2, 4, 0],
    [-1, 0, 2]
    ]
A = np.array(A)

# x = [-0.5, 1]
x = [0, 0, 0]
x = np.array(x)

#print np.dot(x.T, b)

g = fun_grad(x)
d = -g

while np.dot(g.T, g) > 0.01 or np.dot(g.T, g) < -0.01 :
    lambdak = -np.dot(g.T, d) * 1.0 / (np.dot(np.dot(d.T, A), d))
    print "d", d
    x = x + lambdak * d # x(k+1) = x(k) + lambdak * d(k)
    print x
    g = fun_grad(x)
    betak = np.dot(np.dot(d.T, A), g) / np.dot(np.dot(d.T, A), d)
    d = -g + betak * d