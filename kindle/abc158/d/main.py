from collections import deque
s = input()
q= int(input())

d = deque(list(s))

inv = False

for i in range(q):
    query = list(input().split())
    t = int(query[0])
    if t == 1:
        if inv == False:
            inv = True
        else:
            inv = False
            
    else:
        f = int(query[1])
        
        if inv == False:
            if f == 1:
                d.appendleft(query[2])
            else:
                d.append(query[2])
        else:
            if f == 1:
                d.append(query[2])
            else:
                d.appendleft(query[2]) 

if inv == True:
    d.reverse()
    
print("".join(d))