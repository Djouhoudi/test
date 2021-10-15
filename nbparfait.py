import sys
a=int(sys.argv[1])
somdiv=0
for i in range(1,a):
    if a%i==0:
        somdiv=i+somdiv
if somdiv==a:
    print(f"le nombre {a} est parfait")

