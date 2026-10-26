class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        for i in range(1, len(self.nums)):
            self.nums[i] = self.nums[i - 1] + self.nums[i]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """


        if left == 0:
            return self.nums[right]
        return self.nums[right] - self.nums[left - 1]
def main():
    #Your NumArray object will be instantiated and called as such:
    nums = list([-2,0,3,-5,2,-1])
    right = 5
    left = 2
    obj = NumArray(nums)
    param_1 = obj.sumRange(left,right)
    print(param_1)
if __name__ == "__main__":
    main()