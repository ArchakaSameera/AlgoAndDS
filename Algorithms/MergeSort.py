"""
    
    T(n) = 2 T(n/2) + n      n: time spent on merging 

    Time: O(n log n) : Merge n elements log n times
    Space: O(n + log n) = O(n) : log n for recursive call depth, n for temporary list

    n: number of elements to sort
"""

class MergeSort():

    def merge_sort(self, nums):
        if not nums:
            return nums
        tmp = nums[:]
        self._merge_sort_helper(0, len(nums) - 1 ,nums, tmp)


    def _merge_sort_helper(self, low, high, nums, tmp):
        if low < high:
            mid = low + ((high - low) // 2)
            self._merge_sort_helper(low, mid, nums, tmp)
            self._merge_sort_helper(mid + 1, high, nums, tmp)
            self._merge(low, mid, high, nums, tmp)


    def _merge(self, low, mid, high, nums, tmp):
        i, j, k = low, mid + 1, low

        while i <= mid and j <= high:
            if nums[i] < nums[j]:
                tmp[k] = nums[i]
                i += 1
            else:
                tmp[k] = nums[j]
                j += 1
            k += 1

        while i <= mid:
            tmp[k] = nums[i]
            i += 1
            k += 1

        while j <= high:
            tmp[k] = nums[j]
            j += 1
            k += 1

        for i in range(low, k):
            nums[i] = tmp[i]

# sorts in-place
nums = [6,4,1,2,8,5]
obj = MergeSort()
obj.merge_sort(nums)
print(nums)
