# Temperature converter.

temperature = float(input("Digite a temperatura atual em Graus Ceusius: "))
convertedTemperature = (temperature * 1.8) + 32

def Thermometer():
    print(f"A temperatura está em {convertedTemperature} graus Fahrenheit")
    if temperature > 30:
        print(f"A temperatura {temperature} é considerada quente.")
    elif temperature < 15:
        print("A temperatura é considerada fria.")
    else:    
        print("A temperatura está agradável.")

def Line():
    lines = "="
    print(lines*30)

Line()
Thermometer()
Line()