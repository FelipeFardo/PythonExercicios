import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print( f'O ângulo {angulo} possui seno: {seno:.2f}, coseno: {cos:.2f} e tangente: {tang:.2f}')