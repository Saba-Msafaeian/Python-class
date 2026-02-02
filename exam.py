scores = []

for i in range (3):
    a = int(input())
    scores.append(a)
    
sum = 0 

for i in scores:
    sum +=i
    
avg = sum / 3
print(avg)