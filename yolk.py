arts=int(input())
brti=[int(sat) for sat in input().split()]
brti.sort()
sat=0
avt=0
for i in range(len(brti)):
    if brti[i]>=sat:
        avt+=1
    sat=sat+brti[i]
print(avt)
