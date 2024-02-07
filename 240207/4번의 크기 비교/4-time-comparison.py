a=int(input())
b,c,d,e = tuple(map(int, input().split()))
result_b = 1 if a > b else 0
result_c = 1 if a > c else 0
result_d = 1 if a > d else 0
result_e = 1 if a > e else 0

print(result_b)
print(result_c)
print(result_d)
print(result_e)