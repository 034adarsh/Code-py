n = int(input())
if n == 2:
    print(2)
if n > 2:
    for i in range(2, n+1):
        if (n %  i == 0):
            for j in range(2,i):
                if (i % j == 0):
                    break
            else:
                print(i)
