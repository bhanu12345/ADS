n, j = 0,1
total = 0

while True:
    n = n + j  
    j = n + j     
    if j < 4000000:
        total += even
    else:
        break
print total
