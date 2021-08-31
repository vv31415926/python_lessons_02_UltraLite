# Переписать все конструкции используемые в уроке.

for i in range(10):
    print(i)
# -----------------------------------------


horsepower = int(  input('Ввести мощность: '))
tax = 0
if horsepower < 80:
    tax = 0
elif  horsepower < 100:
    tax = 10000
else:
    tax = 50000
print(tax)

itog = 'Дешево' if tax < 40000 else 'Дорого'

print(itog)

# ------------------------------------------------------------

i = 0

while i < 10:
    print(i)
    i = i + 1
    if i == 5:
        break