# problem 6
# initial value problem
# we are solving y1,y2 in the form [y1,y2] at x

from scipy.integrate import solve_ivp
import matplotlib.pyplot as pt
import numpy as np

def f(x,y): # derivatives
 return(np.hstack((32*y[0]+66*y[1]+2/3*x+2/3,-66*y[0]-133*y[1]-x/3-1/3)))

# solving ODEs using scipy
soln=solve_ivp(f,[0,0.5],[1/3.0,1/3.0])

pt.subplot(1,2,1)
pt.plot(soln.t,soln.y[0],'m.-',label="y1")
pt.plot(soln.t,soln.y[1],'c.-',label="y2")
pt.legend();pt.xlabel("x"); pt.ylabel("y(x)");pt.title("Solutions")

pt.subplot(1,2,2)
dy1=np.diff(soln.y[0])
dy2=np.diff(soln.y[1])
dx=np.diff(soln.t)
f1=np.zeros((2,soln.t.size))
for i in range(soln.t.size):
 x=soln.t[i]
 f1[0][i]=32*soln.y[0][i]+66*soln.y[1][i]+2/3*x+2/3
 f1[1][i]=-66*soln.y[0][i]-133*soln.y[1][i]-x/3-1/3
pt.plot(soln.t,f1[0],'y-',label="dy1/dx")
pt.plot(soln.t[1:],dy1/dx,'b.',label="numerical dy1/dx")
pt.plot(soln.t,f1[1],'g-',label="dy2/dx")
pt.plot(soln.t[1:],dy2/dx,'r.',label="numerical dy2/dx")
pt.legend();pt.xlabel("x");pt.ylabel("dy/dx");pt.title("Differentiation")
pt.tight_layout()
pt.show()
