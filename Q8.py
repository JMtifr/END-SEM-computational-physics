# Problem 8
# Boundary value problem
# We will solve ODE by converting it into 2 1st order ODE in [y,y'] form 
from scipy.integrate import solve_bvp
import numpy as np

# defining functions
def f(x,y): # d2y/dx2
 return np.vstack((y[1], 4.0*(y[0]-x)))
def ex(x): # exact solution
 return(np.e**2/(np.e**4-1.0)*(np.exp(2*x)-np.exp(-2*x))+x)
def bc(ya,yb): # boundary conditions
 return(np.array([ya[0]-0.0, yb[0]-2.0]))

# solving ODE using scipy
x=np.linspace(0,1,11) # x array
y=np.zeros((2,x.size))
for i in range(x.size): # initial guess
 y[0][i]=2*i
 y[1][i]=2
soln=solve_bvp(f,bc,x,y)

# printing error
print("Relative errors are \n-------------------------\n  x           error\n______________________________")
for i in range(1,soln.x.size-1):
 print("%1.2f"%soln.x[i]," - ", (soln.y[0][i]-ex(soln.x[i]))/ex(soln.x[i])*100," %")

