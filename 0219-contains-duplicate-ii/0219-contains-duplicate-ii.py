class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen:
                if i - seen[nums[i]] <= k:
                    return True
            seen[nums[i]] = i
        return False


       

        # while l<(len(nums)-1):
        #     r=l+1
        #     while r<len(nums):
        #         if nums[l]==nums[r] and ((r-l) <= k):
        #             return True
        #         r+=1
        #     l+=1
        # return False
            
            

        


        