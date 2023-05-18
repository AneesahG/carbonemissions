import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize
import math

#Quadratic Model
file = "/content/Emissions post 1940.csv"
data = np.loadtxt(file,delimiter = ",",skiprows = 1, unpack = True) 
Year = data[0]
CO2 = data[1]
t = Year - 1940
plt.scatter(t, CO2)
plt.xlabel("Years since 1940")
plt.ylabel("CO2 Concentrations")
plt.xlim(-5,90)
def h(theta):
  a = theta[0]
  b = theta[1]
  c = theta[2]
  sse = 0.0
  def quad(t):
    return(a*t**2 + b*t + c) 
  for i in range(0,len(CO2)):
    sse += (CO2[i]-quad(t[i]))**2
  return(sse)
result = optimize.minimize(h,[1,1,1])
print(result)

a = result.x[0]
b = result.x[1]
c = result.x[2]
def quad(t):
  return(a*t**2 + b*t + c) 
plt.plot(t,quad(t),color = 'red')
