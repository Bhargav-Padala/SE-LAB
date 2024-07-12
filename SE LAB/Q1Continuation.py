import numpy as np
import matplotlib.pyplot as plt
def quadratic_models(time,a,b,c):
    temp = a* (time ** 2) + b * time + c
    return temp
def main() :
        
    time_values = np.linspace(0,10,50)

    with open('C:\Python\CN LAB\SE LAB\Q1SE.txt', 'r') as file:
            lines = file.readlines()
        
    for i, line in enumerate(lines):
            a, b, c = map(float, line.split())
            temperature_file_multiple = quadratic_models(time_values, a, b, c)
            plt.plot(time_values, temperature_file_multiple, label=f'File Input Set {i+1} Coefficients')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Multi Set from File')
    plt.show()

main()
