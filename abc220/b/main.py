
k = int(input())
a,b = map(int,input().split())

base_10_a = int(str(a),k)
base_10_b = int(str(b),k)
print(base_10_a*base_10_b)