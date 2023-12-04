con = [chr(i) for i in range(97,123)]
vow = ['a','e','i','o','u']
for i in vow:
    con.remove(i)

dic = {}
for i in con:
    dic[i] = 1
for i in vow:
    dic[i] = 0

while 1:
    a = input()
    switch = 0
    if a == 'end':
        break
    
    for i in a:
        if i in vow:
            switch = 1
            break
    
    for j in range(len(a)-2):
        if dic[a[j]] == dic[a[j+1]] == dic[a[j+2]]:
            switch = 0
            break
        
    for k in range(len(a)-1):
        if a[k] == a[k+1] == 'e' or a[k] == a[k+1] == 'o':
            continue
        elif a[k] == a[k+1]:
            switch = 0
            break
            
    if switch == 0:
        print(f"<{a}> is not acceptable.")
    else:
        print(f"<{a}> is acceptable.")