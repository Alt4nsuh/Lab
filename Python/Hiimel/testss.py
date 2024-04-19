from typing import List

class Solution:
    def supp(self, arr, j):
        for i in arr:
            j = j ^ i
        return j 

    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        arr = [0] * n
        arr[0] = pref[0]
        for i in range(1, n):
            arr[i] = self.supp(arr, pref[i])
        return arr

# Example usage
if __name__ == "__main__":
    solution = Solution()
    pref_input = [5, 2, 0, 3, 1]
    result = solution.findArray(pref_input)
    print("Result:", result)
