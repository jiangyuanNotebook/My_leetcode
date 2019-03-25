

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # dict = {}
        # # 数组元素放入hash表
        # for i in range(len(nums)):
        #     dict[nums[i]] = i
        # print(dict)
        # r = []
        # # 遍历数组从hash表中找另一个数的索引
        # for i in range(len(nums)):
        #     n = target - nums[i]
        #     if n in dict and dict[n] != i:
        #         r.append(i)
        #         r.append(dict[n])
        #         return r
        numsize = len(nums)
        a = list(range(numsize))
        di = dict(zip(nums,a))
        print(di)
        # for k in di.keys():
        for i in range(numsize):
            findnum = target - nums[i]
            if(di.get(findnum)!=None and di.get(findnum)!=i):
                return [i,di.get(findnum)]

        return []

    # def twoSum1(self, nums: List[int], target: int) -> List[int]:
    #     hashmap = {}
    #     res = []
    #     for index, num in enumerate(nums):
    #         if num not in hashmap:
    #             hashmap[target - num] = index
    #         else:
    #             res.append(index)
    #             res.append(hashmap[num])
    #     return res
def main():
    nums = [2,2]
    target = 4
    so = Solution()
    re = so.twoSum(nums,target)
    print(re)

if __name__ == '__main__':
    main()