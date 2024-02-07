a,b =tuple(map(int, input().split()))

bmi = b * 100 * 100 // (a * a)

# 출력
print(bmi)
if bmi >= 25:
	print("Obesity")