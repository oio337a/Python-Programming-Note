# 재귀
def fibo_rec(x):
	if x == 1 or x == 2:
		return 1
	else:
		return fibo_rec(x - 1) + fibo_rec(x - 2)

print("---------------")

# 재귀 메모이제이션
d = [0] * 100

def fibo_rec_memo(x):
	if x == 1 or x == 2:
		return 1
	if d[x] != 0:
		return d[x]
	d[x] = fibo_rec_memo(x - 1) + fibo_rec_memo(x - 2)
	return d[x]



print("---------------")

# 반복문 메모이제이션
def fibo_2(x):
	d = [0] * (x + 1)
	
	d[1], d[2] = 1, 1

	for i in range(3, x + 1):
		d[i] = d[i - 1] + d[i - 2]
	return d[x]

print(fibo_2(7))