n,a,b = map(int,input().split())
p,q,r,s = map(int,input().split())

k_min_m = max(1-a,1-b)
k_max_m = min(n-a,n-b)

k_min_p = max(1-a,b-n)
k_max_p = min(n-a,b-1)

# max(1−A,1−B)≤k≤min(N−A,N−B) 
a_p_max = k_max_m + a-1
a_p_min = k_min_m + a-1

b_p_max = k_max_m + b-1
b_p_min = k_min_m + b-1

#max(1−A,B−N)≤k≤min(N−A,B−1) 
a_m_max = k_max_p + a -1
a_m_min = k_min_p + a -1

b_m_max = -k_max_p + b -1
b_m_min = -k_min_p + b -1

range_x = range(min(a_p_min,p),min(a_m_max,q))
range_y = range(min(b_p_min,r),min(b_p_max,s))
print(range_x,range_y)


# print(a_p_max,a_p_min)
# print(b_p_max,b_p_min)

# print(a_m_max,a_m_min)
# print(b_m_max,b_m_min)

for i in range(p,q):
  ans = ""
  for j in range(r,s):
    for kx in range(min(p,a_p_min),max(q,a_p_max)):
      for ky in range(min(r,b_p_min),max(s,b_p_max)):
        