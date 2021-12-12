def c(st):
    l = len(st)
    for i in range(l//2):
        if st[i] != st[l-i-1]:
            return 0
    else:
        return 1


s = input()
n = len(s)
print(["No", "Yes"][c(s)*c(s[:n//2])*c(s[n//2+1:])])
