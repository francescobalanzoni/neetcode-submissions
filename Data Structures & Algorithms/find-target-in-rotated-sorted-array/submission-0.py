class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        cut = l

        if nums[cut] <= target <= nums[-1]:
            l, r = cut, len(nums) -1
        else:
            l, r = 0, cut

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        
        return -1



        