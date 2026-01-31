class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list1=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(j==i):
                    break
                else:
                    result=nums[j]+nums[i]
                    if(result==target):
                        list1.append(i)
                        list1.append(j)
                    else:
                        continue
        return list1
