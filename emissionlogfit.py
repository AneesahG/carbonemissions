import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize
import math

#Temperature- emissions log fit
file = "/content/Temp match CO2.csv"
data1 = np.loadtxt(file,delimiter = ",",skiprows = 1, usecols = (0,1), unpack = True) 
Temperature = data1[1]
file = "/content/Emissions post 1940.csv"
data2 = np.loadtxt(file,delimiter = ",",skiprows = 1, unpack = True) 
CO2 = data2[1]
plt.scatter(CO2,Temperature)
plt.xlabel("CO2 Concentration")
plt.ylabel("Global Average Temperature Anomaly")
def h(theta):
  a = theta[0]
  b = theta[1]
  c = theta[2]
  sse = 0.0
  def log(t):
    return(a*np.log(b*t) + c) 
  for i in range(0,len(Temperature)):
    sse += (Temperature[i]-log(CO2[i]))**2
  return(sse)
result = optimize.minimize(h,[1,1,1])
print(result)

a = result.x[0]
b = result.x[1]
c = result.x[2]
def log(t):
    return(a*np.log(b*t) + c)
plt.plot(CO2,log(CO2),color = 'red')
