class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in seen:
                return [seen[needed], i]
            seen[nums[i]] = i
        return [-1, -1]


        return None
def main():
    nums = [2, 7, 11, 15]
    target = 9
    obj = Solution()
    print(obj.twoSum(nums, target))
if __name__ == "__main__":
    main()