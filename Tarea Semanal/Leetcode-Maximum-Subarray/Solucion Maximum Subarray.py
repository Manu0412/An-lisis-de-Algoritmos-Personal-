class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        """
        Complejidad Espacial O(1) 
        Complejidad Temporal O(n)
        Se recorre el arreglo y se acumula la suma máxima contigua usando el algoritmo de Kadane.
        """
        max_actual = nums[0]
        max_global = nums[0]

        for i in range(1, len(nums)):
            max_actual = max(nums[i], max_actual + nums[i])
            max_global = max(max_global, max_actual)

        return max_global
