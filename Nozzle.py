import math
#Nozzle performance
g=9.8
#inputs
Pc=float(input("Chamber Pressure [Pa] [2000000.0]: ",) or "2000000.0")
Tc=float(input("Chamber Temperature [K] [3000]: ") or "3000.0")
gamma=float(input("Specific heat ratio [1.2]: ") or "1.2")
Pa=float(input("Ambient pressure {Pa} [101325.0]: ") or "101325.0")
Cp=float(input("Specific heat constant [J/KgK] [287]: ") or "287.0")
Dt=float(input("Throat diameter {m} [40]: ") or "40.0")
De=float(input("Exit diameter {m} [80]: ") or "80.0")

#Calculations
print("Nozzle performance: ")
#area ratio exit to throat
Ar=(De/Dt)**2
Ae=(3.14*((De/2)**2))
At=(3.14*((Dt/2)**2))
#gas constant
R=(gamma-1)*Cp/gamma
#exit mach number (approximation)
Me=((2/(gamma-1))*((Ar**(gamma-1))-1))**(1/2)
print("exit Mach Number: ",Me)
#exit pressure
Pe=Pc*((1+(((gamma-1)/2)*(Me**2)))**((0-gamma)/(gamma-1)))
print("Exit Pressure {Pa} : ", Pe)
#Exit temp
Te=Tc*((1+((gamma-1)/2)**(Me**2))**(0-1))
print("Exit temp [K]: ", Te)
#Exit velocity
Ve=Me*math.sqrt(gamma*R*Tc/(1+(gamma-1)/2*Me**2))
print("Exit velocity [m/s]: ", Ve)
#Mass flow rate
Mf= At*Pc*math.sqrt(gamma/(R*Tc))*(2/(gamma+1))**((gamma+1)/(2*(gamma-1)))
print("Mass flow rate [Kg/s]: ", Mf)
#Thrust
F=Mf*Ve+(Pe-Pa)*Ae
print("Thrust {n}: ", F)
#ISP
Isp=F/(Mf*g)
print("Specific impulse [s]: ", Isp)