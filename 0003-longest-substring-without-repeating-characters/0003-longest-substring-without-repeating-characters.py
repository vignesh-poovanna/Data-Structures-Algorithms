class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l =0
        r =0
        seen = set()
        ans = 0

        while r<len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r+=1
                if len(seen)> ans:
                    ans = len(seen)
            elif s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l +=1
                seen.add(s[r])
                r += 1

        return ans
