x = int(input("Digite o valor: B$ "))

n50 = x // 50
r = x % 50
n10 = r // 10
r = r % 10
n5 = r // 5
n1 = r % 5

print(n50,"nota(s) de B$ 50")
print(n10,"nota(s) de B$ 10")
print(n5,"nota(s) de B$ 5")
print(n1,"nota(s) de B$ 1")