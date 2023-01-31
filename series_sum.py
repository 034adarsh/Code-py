#sum of 1+(1+2)+(1+2+3)+...+n terms.
n = int(input())
total = 0
for i in range(1, n + 1):
    for j in range(1,i+1):
        total = total + j
print(total)
