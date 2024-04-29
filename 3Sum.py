class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
	#1. Split nums into three lists: negative numbers, positive numbers, and zeros
        negative = []
        positive = []
        zeros = []
        for num in nums:
            if num > 0:
                positive.append(num)
            elif num < 0:
                negative.append(num)
            else:
                zeros.append(num)
	#2. Create a separate set for negatives and positives for O(1) look-up times
        Negative , Positive = set(negative) , set(positive)
        if zeros:
            for num in Positive:
                if -1 * num in Negative:
                    result.add((-1*num, 0, num))
    #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if len(zeros) >= 3:
            result.add((0,0,0))
    #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
	#   exists in the positive number set
        for i in range(len(negative)):
            for j in range(i + 1, len(negative)):
                target = -1*(negative[i] + negative[j])
                if target in Positive:
                    result.add(tuple(sorted([negative[i],negative[j],target])))
    #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
	#   exists in the negative number set
        for i in range(len(positive)):
            for j in range(i + 1, len(positive)):
                target = -1*(positive[i] + positive[j])
                if target in Negative:
                    result.add(tuple(sorted([positive[i],positive[j],target])))
        return result  
