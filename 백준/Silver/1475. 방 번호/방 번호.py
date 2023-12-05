n = input()
number = [0]*10
for i in n:
    number[int(i)] += 1
    
x = number[9]
del number[9]
y = number[6]
del number[6]

if (x+y+1)//2 > max(number):
    print((x+y+1)//2)
else:
    print(max(number))