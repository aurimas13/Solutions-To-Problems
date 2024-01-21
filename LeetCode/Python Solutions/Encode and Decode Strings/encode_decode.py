class Codec:

    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ret_str = ""
        lens = [str(len(s)) for s in strs]
        return ",".join(lens) + "#" + "".join(strs)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        index = s.index("#")
        lens = s[:index].split(",")
        ans = []
        start = index + 1
        for l in lens:
            l = int(l)
            ans.append(s[start:start + l])
            start += l
        return ans

# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    codec = Codec()
    print((codec.decode(codec.encode(["Hello","World"])))) # ["Hello","World"] -> ["Hello","World"]
