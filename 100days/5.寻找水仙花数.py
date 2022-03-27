

for i in range(100,1000):
    high=i//100
    mid=(i-high*100)//10
    low=i-high*100-mid*10
    if high**3+mid**3+low**3==i:
        print(i)
