#aphabets are mapped to numbers starting from 0-9.
# for example a=0, b=1 till j=9 then again k=0 and so on...

s1 = input()
x = [*s1]
i=0
for i in x:
  y= ord(i)
  print(str((y-97)%10), end ='')
