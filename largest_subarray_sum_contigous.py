# Suppose an array [-2, -3, 4, -1, -2, 1 , 5 , -3]
# We use Kadanes algorithm to determine the sum of contigous array element
# Recurence Relation defined max(sum[i-1]+A[i], A[i])
# Since we are considering both positive and negative
# we can either include a number or exclude a number


nums = [-2, -3, 4, -1, -2, 1 , 5 , -3]
# max sum = 7

maxHere = 0
maxVal = 0

for i in xrange(0,len(nums)):
	maxHere = max(maxHere + nums[i], nums[i])
	maxVal = max(maxVal, maxHere)

print(maxVal)