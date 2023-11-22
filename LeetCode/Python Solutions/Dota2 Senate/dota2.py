class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Convert input string to lists of indices for each party
        radiant = [i for i, c in enumerate(senate) if c == 'R']
        dire = [i for i, c in enumerate(senate) if c == 'D']

        # Iterate until one party has no more senators
        while radiant and dire:
            # Compare the first senator of each party
            if radiant[0] < dire[0]:
                radiant.append(radiant.pop(0) + len(senate))  # Move this senator to the back
                dire.pop(0)  # Eliminate the first senator of the opposite party
            else:
                dire.append(dire.pop(0) + len(senate))  # Move this senator to the back
                radiant.pop(0)  # Eliminate the first senator of the opposite party

        # Return the winning party based on which list still has senators
        return "Radiant" if radiant else "Dire"


def test_solution():
    solution = Solution()

    assert solution.predictPartyVictory("RD") == "Radiant"
    assert solution.predictPartyVictory("RDD") == "Dire"
    assert solution.predictPartyVictory("RRDD") == "Radiant"
    assert solution.predictPartyVictory("DDRR") == "Dire"
    
    print("All tests passed successfully")

if __name__ == "__main__":
    test_solution()