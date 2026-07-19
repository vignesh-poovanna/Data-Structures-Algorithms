class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        h = {}
        u =[]
        for ele in nums:
            if ele not in h:
                h[ele] = 1
            else:
                h[ele]+=1
        for ele in h:
            if h[ele]==1:
                u.append(ele)
        return u



        