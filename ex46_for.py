#Faça um programa que mostre na tela uma contagem regresiva para estouro de fogos de artificio,
#indo de 10 ate 0, com uma pausa de 1 segundo entre eles
import time
for c in range(10, -1, -1):
    print('#',c,'#')
    time.sleep(1)
print('**#*#BOOM#*#*')

