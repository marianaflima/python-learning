from math import radians, sin, cos, tan

ang = float(input('Digite um ângulo: '))
rad = radians(ang)

print(f'Para o ângulo {ang}°: \n - Seno: {sin(rad):.2f} \n - Cosseno: {cos(rad):.2f} \n - Tangente: {tan(rad):.2f}')