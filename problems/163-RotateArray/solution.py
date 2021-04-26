# nums[:]=nums[-k:]+nums[0:-k]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k%l
        def reverse(nums, left, right):
            while (left < right):
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(nums, 0, l - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, l - 1)

#Solution using queue
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k%l
        q = deque()
        start = l-k
        while start < l :
            q.append(nums[start])
            start += 1
        
        for i in range(l):
            q.append(nums[i])
            nums[i] = q.popleft()