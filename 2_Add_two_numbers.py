# English:
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Spanish:
# Se te dan dos listas enlazadas no vacías que representan dos números enteros no negativos. 
# Los dígitos están almacenados en orden inverso y cada uno de sus nodos contiene un solo dígito. Suma los dos números y devuelve la suma como una lista enlazada.
# Puedes asumir que los dos números no contienen ceros a la izquierda, excepto el número 0 en sí.


l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

solution = []


if (len(l1) > len(l2)):
    l2 += [0] * (len(l1) - len(l2))
elif (len(l1) < len(l2)):
    l1 += [0] * (len(l2) - len(l1))

value = 0
for i in range(len(l1)):
    if value == 0:
        add = l1[i] + l2[i]
        if len(str(add)) > 1:
            solution.append(str(add)[-1])
            value = int(str(add)[:-1])
        else:
            value = 0
            solution.append(add)
    else:
        add = l1[i] + l2[i] +  value
        if len(str(add)) > 1:
            solution.append(str(add)[-1])
            value = int(str(add)[:-1])
        else:
            value=0
            solution.append(add)

if value:
    solution.append(value)
print('l1: ',l1)
print('l2: ',l2)
print('Solution: ',solution)