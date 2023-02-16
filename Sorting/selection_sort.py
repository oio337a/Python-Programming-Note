# 선택 정렬

test_array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(test_array)):
	min_index = i # 가장 작은 원소의 인덱스
	for j in range(i + 1, len(test_array)):
		if test_array[min_index] > test_array[j]:
			min_index = j
	test_array[i], test_array[min_index] = test_array[min_index], test_array[i] # 스왑

print(test_array)