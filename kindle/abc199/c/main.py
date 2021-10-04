n = int(input())
string = input()
q = int(input())

string = "0"+string
string = list(string)

flip=False
 
for i in range(q):
    t,a,b = map(int,input().split())
    if t == 1:
        if flip==False:
            string[a],string[b] = string[b],string[a]
        else:
            if a <= n:
                a += n
            else:
                a-=n
            if b <= n:
                b += n
            else:
                b-=n
            string[a],string[b] = string[b],string[a]
        print("".join(ans))
    else:
        if flip == True:
            flip = False
        else:
            flip = True
        s_left = string[1:n+1]
        s_right = string[n+1:]
        if flip == False:
            ans = s_left+s_right
        else:
            ans = s_right+s_left
        print("".join(ans))