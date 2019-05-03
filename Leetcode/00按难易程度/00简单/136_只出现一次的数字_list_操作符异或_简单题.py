'''
136-只出现一次的数字-简单题

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
输入: [2,2,1]
输出: 1
'''

class Solution(object):
	def singleNumber(self, nums):
		'''
		:type nums: List[int]
		:rtpye: int
		'''
		for i in range(1, len(nums)):
			nums[0] ^= nums[i]
		return nums[0]

'''
简直是神仙方法：
两个相同的取异或，得0，0和任何异或都不变，所有项进行异或，完了肯定是那个就一个的数字
'''