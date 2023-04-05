class Solution:
    def evaluate(self, expression: str) -> int:
        # Function to parse the tokens
        def parse(tokens):
            # Pop the first token and check its type
            token = tokens.pop(0)
            if token == '(':
                # Create a new list and append tokens until we find the matching parenthesis
                lst = []
                while tokens[0] != ')':
                    lst.append(parse(tokens))
                tokens.pop(0)  # Discard the closing parenthesis
                return lst
            else:
                # Return the token as an integer or a variable
                try:
                    return int(token)
                except ValueError:
                    return token

        # Function to evaluate the parsed expression
        def evaluate(parsed, env):
            if isinstance(parsed, int):
                return parsed
            elif isinstance(parsed, str):
                return env[parsed]
            else:
                op = parsed[0]
                if op == 'add':
                    return evaluate(parsed[1], env) + evaluate(parsed[2], env)
                elif op == 'mult':
                    return evaluate(parsed[1], env) * evaluate(parsed[2], env)
                else:  # 'let' operation
                    new_env = env.copy()
                    for i in range(1, len(parsed) - 1, 2):
                        new_env[parsed[i]] = evaluate(parsed[i + 1], new_env)
                    return evaluate(parsed[-1], new_env)

        # Tokenize the expression
        tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()

        # Parse and evaluate the expression
        return evaluate(parse(tokens), {})


# Test cases to try in the terminal/console
if __name__ == '__main__':
    solution = Solution()
    print(solution.evaluate("(add 1 2)"))  # Output: 3
    print(solution.evaluate("(mult 3 (add 2 3))"))  # Output: 15
    print(solution.evaluate("(let x 2 (mult x 5))"))  # Output: 10
    print(solution.evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))"))  # Output: 14
