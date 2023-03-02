n = int(input('Sequência de fibonacci: '))

n1, n2 = 1, 1
cont = 0
while  cont <= n:
    n3 = n1 + n2
    n1, n2 = n2, n3
    cont += 1
    if n3 >= n:
        break

print("---------------------------------------------------------------------------")
if n == n3 or n == 1 or n == 0:
    print(f"O número {n} faz parte da sequêcia de fibonacci!")
else:
    print(f"O número {n} não faz parte da sequêcia de fibonacci!")