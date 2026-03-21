class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        dp[i] representa el máximo dinero que se puede obtener hasta a la casa i
        
        Recurrencia: Para cada casa, se elige entre conservar el máximo anterior o robarla y sumar su valor al máximo obtenido hasta dos casas atrás

       Casos base: Para la primera casa se toma su valor, y para la segunda se elige el máximo entre las dos primeras.

        Complejidad: Tiempo: O(n) y Espacio: O(n)
        """
        if len(nums) == 1:
            return nums[0]
        
        dp= [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i]=max(dp[i-1], nums[i] + dp[i-2])

        return dp[len(dp)-1]
