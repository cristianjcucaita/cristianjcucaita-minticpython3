cont = 0
lista = []
edad = []

n = int(input())
for i in range (0,n):
    a = list(map(int,input().strip().split())) #Ingreso de los datos
    lista.append(a)

#Condicionales de vacunacon inmediata:

# 1. 80 años o mas.
# 2. Diabetes tipo 2 = 7% o mayor.
# 3. Obesidad con indice de 30 o superior.
# 4. Tension sistolica 140mmHg o mas.
# 5. Tension diastolica 90mmHg o mas.

for v in lista:
    if v[0]>=80 and v[1]>7 and v[2]>=30 and v[3]>=140 and v[4]>=90:
        cont += 1
        edad.append(v[0])
if cont == 0:
    print('NO DISPONIBLE')
else:
    for v in edad:
        print(v)