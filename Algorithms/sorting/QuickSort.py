"""
https://www.youtube.com/watch?v=ZHVk2blR45Q

Time:
    Best and Average: O(n log n)
        T(n) = 2 T(n/2) + n

    Worst: O(n^2)
        T(n) = T(n - 1) + n

Space: Because of recursive calls
    Best and Average: O(log n)
    Worst O(n)
"""
class QuickSort():

    def quick_sort(self, nums):
        if not nums:
            return nums
        self._quick_sort_helper(0, len(nums) - 1, nums)


    def _quick_sort_helper(self, lo, hi, nums):
        if lo < hi:
            k = self._partition(lo, hi, nums)
            self._quick_sort_helper(lo, k - 1, nums)
            self._quick_sort_helper(k + 1, hi, nums)


    def _partition(self, lo, hi, nums):
        pivot = nums[hi]
        # i - first element greater than pivot
        # j - current element in comparision
        i, j = lo, lo

        while j < hi:
            if nums[j] <= pivot:
                if i != j:
                    self._swap(nums, i, j)
                i += 1
            j += 1
        self._swap(nums, i, hi)
        return i


    def _swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp


nums = [5,3,1,2,2,8,9,-7,0,15]
obj = QuickSort()
obj.quick_sort(nums)
print(nums)
