class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <=1:
            return s

        num_cycle = 2*numRows - 2
        lines = [[] for i in range(numRows)]            # Create list for every line
        for i, val in enumerate(s):

            curr_cycle = i // num_cycle                 # Calculate current cycle (one cycle is down and up)
            j = i - curr_cycle * num_cycle              # set iterator to current position
            if j >= numRows:
                j = (j-num_cycle)*-1                    # if going upwards correct position for the line

            lines[j].append(val)

        out = ''
        for i in range(numRows):                        # read out lines after each other
            out += ''.join(lines[i])
        return out


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.convert("PAYPALISHIRING", numRows=3) #  s="PAYPALISHIRING", numRows=3 -> "PAHNAPLSIIGYIR"
    print(Solve)
