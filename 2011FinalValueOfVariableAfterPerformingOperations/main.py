class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        num = 0
        for operation in operations:
            if operation == "X++" or operation == "++X":
                num += 1
            else:
                num -= 1
        return num