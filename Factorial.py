n=int(input('Enter a number:'))
fact=1
num=1
while(n>=fact):
  num*=fact
  fact+=1
print(num) 


#other method

n=int(input('Enter a number:'))
fact=1
num=1
if(n<0):
  print('Not defined')
 
else:
  while(n>=fact):
    num*=fact
    fact+=1
  print(num
