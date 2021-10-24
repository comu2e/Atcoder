n = int(input())
button = [False]*(n+1)
button[1] = True
for i in range(n):
    a = int(input())
    if button[a] == False:
        button[a] = True
