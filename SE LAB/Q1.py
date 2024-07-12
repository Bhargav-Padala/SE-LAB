import matplotlib.pyplot as plt 
import numpy as np 
def QTWM(t,a,b,c):
    return (a* t**2 + b*(t+c))

hc_a = 1.0
hc_b = -2.5
hc_c = 3.5
Graph_Values = np.linspace(0,10,100)
hc_temp = QTWM(Graph_Values,hc_a,hc_b,hc_c)
plt.figure(figsize=(10, 6))
plt.plot(Graph_Values, hc_temp, label=f'Hardcoded: a={hc_a}, b={hc_b}, c={hc_c}')

sets = int(input("Enter the number of sets of inputs: "))
Coefficients = []
for i in range (sets):
    print(f"\nSet {i+1}: ")
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))
    Coefficients.append((a,b,c))

for i, (a,b,c) in enumerate(Coefficients):
    Temperature =  QTWM(Graph_Values,a,b,c)
    plt.plot(Graph_Values,Temperature,label = f'Set {i+1}: a={a}, b={b}, c={c}')

plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title ("Weather Modelling using Quadratic Equation")
plt.legend()
plt.grid(True)
plt.show()


