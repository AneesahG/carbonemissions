import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize
import math

#Emissions Exponential fit
file = "/content/Emissions post 1940.csv"
data = np.loadtxt(file,delimiter = ",",skiprows = 1, unpack = True) 
Year = data[0]
CO2 = data[1]
t = Year - 1940
plt.scatter(t, CO2)
plt.xlabel("Years since 1940")
plt.ylabel("CO2 Concentrations")
plt.xlim(-5,90)
#Exponential model
def h(theta):
  a = theta[0]
  b = theta[1]
  sse = 0.0
  def exponential(t):
    return(a*np.exp(b*t))
  for i in range(0,len(CO2)):
    sse += (CO2[i]-exponential(t[i]))**2
  return(sse)
result = optimize.minimize(h,[300.,0.01])
print(result)

a = result.x[0]
b = result.x[1]
def exponential(t):
  return(a*np.exp(b*t))
plt.plot(t,exponential(t))

