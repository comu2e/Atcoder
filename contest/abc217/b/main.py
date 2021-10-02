all = ["ABC","ARC","AGC","AHC"]
contests = []
for i in range(3):
    contests.append(input())
 
print(list(set(all)^set(contests))[0])