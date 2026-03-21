class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        dp[i] representa el costo mínimo para llegar al escalón i
        Recurrencia: Se elige el camino más barato entre subir un paso o dos pasos
        Casos base: El costo para empezar en los dos primeros escalones es cero
        Complejidad: Tiempo: O(n) y Espacio: O(n)
        """
        n = len(cost)
        dp = [0] * (n + 1)

        dp[0] = 0
        dp[1] = 0

        for i in range(2, n + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[n]
