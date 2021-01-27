fibonacci = []


sum_num = 0
for x in range(20):
    if x == 0:
        fibonacci.append(0)
    elif x == 1 or x == 2:
        fibonacci.append(1)
    elif x > 2 and sum_num < 55:
        sum_num = fibonacci[x-1] + fibonacci[x-2]
        fibonacci.append(sum_num)
       
print(fibonacci)     
            
   
