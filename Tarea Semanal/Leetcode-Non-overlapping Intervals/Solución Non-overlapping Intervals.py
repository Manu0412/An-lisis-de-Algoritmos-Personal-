class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        """
        Complejidad Temporal: O(n log n)
        Complejidad Espacial: O(1)
        Se ordenan los intervalos por su final y se recorren comparando con el último intervalo válido; si se solapan, se cuenta como eliminado, lo que minimiza los solapamientos y deja más espacios para los siguientes. 
        """

        intervals.sort(key=lambda x: x[1])
        count = 0
        prev_end = intervals[0][1]

        for i in range (1, len(intervals)):
            if intervals[i][0] < prev_end:
                count += 1
            else:
                prev_end = intervals[i][1]

        return count
