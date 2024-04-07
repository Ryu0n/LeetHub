class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mem = dict()
        mlen = 1 if len(s) > 0 else 0
        for i in range(len(s)-1):
            mem.clear()
            mem[s[i]] = 1
            for j in range(i+1, len(s)):
                if mem.get(s[j]) is not None:
                    break
                mem[s[j]] = 1
            if len(mem) > mlen:
                mlen = len(mem)
        return mlen