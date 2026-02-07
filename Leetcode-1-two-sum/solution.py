class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
        Complejidad O(n) itera n veces sobre la lista usando un diccionario
        """

        numVistos = {}

        for i, num in enumerate(nums):
            comp = target - num

            if comp in numVistos:
                return [numVistos[comp], i]

            numVistos[num] = i
