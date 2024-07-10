class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for log in logs:
            if log == "../":
                if depth > 0:
                    depth -= 1
            elif log != "./":
                depth += 1
        return depth
