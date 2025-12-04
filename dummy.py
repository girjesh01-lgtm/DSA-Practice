
class Solution:
    def twoSum(self, arr, target):
        # code here
        pair_exists = False
        hashset = set()
        for item in arr:
            diff = target - item
            if diff in hashset:
                print(f"diff = {diff}, item={item}, target={target}, hashset={hashset}")
                pair_exists = True
                break
            else:
                hashset.add(item)
                print(f"hashset {hashset}, item {item}")
        return pair_exists

s = Solution()
print(s.twoSum(arr=[1,-2,1,0,5], target=0))

#5kKZ2u!{
#888086806350