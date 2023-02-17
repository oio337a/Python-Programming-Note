# ------------------------------ #
'''
  case 1 : basic (recursive)
'''

# 이진 탐색 재귀
def binary_search(arr, target, start, end):
	if start > end:
		return None
	mid = (start + end) // 2
	# 찾은 경우 인덱스 반환
	if arr[mid] == target:
		return mid
	# 중간점의 값보다 찾고자 하는 값이 작은 왼쪽 확인
	elif arr[mid] > target:
		return binary_search(arr, target, start, mid - 1)
	# 중간점의 값보다 찾고자 하는 값이 클경우 오른쪽 확인
	else:
		return binary_search(arr, target, mid + 1, end)

# 전체 리스트의 사이즈, 찾을 값 입력받기
size, target = map(int, input().split())

# 전체 원소 입력 받기
arr = list(map(int, input().split()))

result = binary_search(arr, target, 0, size - 1)
if result == None:
	print("찾고자 하는 값이 없습니다.")
else:
	print(result + 1)

# ------------------------------ #
'''
  case 1 : basic (loop)
'''

# 이진 탐색 반복문
def binary_searsh(arr, target, start, end):
	while start <= end:
		mid = (start + end) // 2
		# 찾은 경우 중간점 인덱스 반환
		if arr[mid] == target:
			return mid
		# 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
		elif arr[mid] > target:
			end = mid - 1
		# 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽  확인
		else:
			start = mid + 1
	return None

# 전체 리스트의 사이즈, 찾을 값 입력받기
size, target = map(int, input().split())

# 전체 원소 입력 받기
arr = list(map(int, input().split()))

result = binary_search(arr, target, 0, size - 1)
if result == None:
	print("찾고자 하는 값이 없습니다.")
else:
	print(result + 1)