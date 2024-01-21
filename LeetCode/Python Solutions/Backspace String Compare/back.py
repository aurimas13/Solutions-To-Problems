class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Helper function to apply backspaces to the input string
        def process_string(string: str) -> str:
            stack = []

            # Iterate through the string characters
            for char in string:
                if char == '#':
                    # If a backspace is encountered, pop the last element from the stack
                    if stack:
                        stack.pop()
                else:
                    # Otherwise, add the character to the stack
                    stack.append(char)

            # Return the processed string as a result
            return "".join(stack)

        # Apply the process_string function to both input strings and compare the results
        return process_string(s) == process_string(t)


if __name__ == "__main__":
    s = Solution()

    # Test cases
    test_cases = [
        ({"s": "ab#c", "t": "ad#c"}, True),
        ({"s": "ab##", "t": "c#d#"}, True),
        ({"s": "a##c", "t": "#a#c"}, True),
        ({"s": "a#c", "t": "b"}, False),
    ]

    for i, (test_input, expected_output) in enumerate(test_cases):
        result = s.backspaceCompare(**test_input)
        assert result == expected_output, f"Test case {i} failed: expected {expected_output}, got {result}"
        print(f"Test case {i} succeeded")
