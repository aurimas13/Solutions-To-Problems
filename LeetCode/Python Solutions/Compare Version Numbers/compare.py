class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))

        # Extend the shorter list with zeros
        max_length = max(len(v1), len(v2))
        v1.extend([0] * (max_length - len(v1)))
        v2.extend([0] * (max_length - len(v2)))

        # Compare versions
        for i in range(max_length):
            if v1[i] < v2[i]:
                return -1
            elif v1[i] > v2[i]:
                return 1

        return 0
