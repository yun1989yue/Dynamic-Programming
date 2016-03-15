'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint 
stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob 
tonight without alerting the police.

'''
'''
Idea：O(n) time O(1) space
consider maxPro[i] is max cash robbed before ith house
maxPro[i-1] is max cash robbed without ith house 
maxPro[i-2] + nums[i] is max CASH robbed with ith house
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        pre1 = nums[0] # since we only need two previous cases, no need to record every previous cases
        pre2 = max(nums[0],nums[1])
        for i in xrange(2, len(nums)):
            key = max(pre1 + nums[i], pre2)
            pre1 = pre2
            pre2 = key
        return pre2
        
'''
After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much 
attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
Meanwhile, the security system for these houses remain the same as for those in the previous street. 

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob 
tonight without alerting the police.
'''
'''
Idea:
The difference between I and II is that the 1st house and the last house can be robbed at the same time in I but not in II
Hence maxPro[2<->n-2]+nums[0] is max cash robbed with 1st house
maxPro[1<->n-1] is max cash robbed without 1st house
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 4:
            return max(nums)
        pro1 = self.robOne(nums, 2, len(nums)-2)+nums[0]
        pro2 = self.robOne(nums, 1, len(nums)-1)
        return max(pro1, pro2)
        
    def robOne(self, nums, start, end):
        if start == end:
            return nums[start]
        if start + 1 == end:
            return max(nums[start],nums[end])
        pre1 = nums[start]
        pre2 = max(nums[start],nums[start+1])
        for i in xrange(start+2, end+1):
            key = max(pre1 + nums[i], pre2)
            pre1 = pre2
            pre2 = key
        return pre2
