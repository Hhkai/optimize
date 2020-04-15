import numpy as np
import matplotlib.pyplot as plt

a1 = 2
b1 = 5

def grad(x):
    x1 = x[0]
    x2 = x[1]
    f_dashx1 = -2*(a1-x1)-4*b1*(x2-x1*x1)*x1
    f_dashx2 = 2*b1*(x2-x1*x1)
    return np.array([f_dashx1, f_dashx2])
def Hess(x):
    x1 = x[0]
    x2 = x[1]
    x1x1 = 2-4*b1*x2+12*b1*x1*x1 
    x1x2 = -4*b1*x1 
    x2x2 = 2*b1 
    return np.array([[x1x1, x1x2],[x1x2, x2x2]])
x_list = []
def SteepestDescent(x, grad, Hess):
    g = grad(x)
    leng = np.dot(g.T, g)
    iter = 1
    while leng > 0.1 or leng < -0.1 :
        d = g * -1 
        lambdak = -np.dot(g.T, d) * 1.0 / (np.dot(np.dot(d.T, Hess(x)), d))
        x_next = x + lambdak * d # x(k+1) = x(k) + lambdak * d(k)
        
        x = x_next
        g = grad(x) 
        leng = np.dot(g.T, g)
        iter += 1
        
        x_list.append(x)
    print(x[0],x[1],g[0],g[1],leng)
#
x=np.array([0,0])
x_list.append(x) 
SteepestDescent(x, grad, Hess)
#exit()
plt.xlim(-1, 3)
plt.ylim(-1, 3)
for p in x_list:
    plt.plot(x[0], x[1], "o")
for i in range(len(x_list) - 1):
    dx = x_list[i+1][0] - x_list[i][0]
    dy = x_list[i+1][1] - x_list[i][1]
    plt.quiver(x_list[i][0], x_list[i][1], dx, dy, angles='xy', scale=1.03, scale_units='xy', width=0.005)
    
plt.show()






















#print("<tr><td align=center>%d</td>\n<td align=center>(%.6f, %.6f)</td>\n<td align=center>(%.6f, %.6f)</td>\n<td align=center>%.6f</td>\n<td align=center>(%.6f, %.6f)</td><td align=center>%.6f</td></tr>" % (iter, x[0],x[1],g[0],g[1],leng,d[0],d[1], lambdak))